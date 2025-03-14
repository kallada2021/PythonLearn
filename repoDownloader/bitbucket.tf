# main.tf

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
    bitbucket = {
      source  = "DrFaust92/bitbucket"
      version = "~> 2.0"
    }
    null = {
      source  = "hashicorp/null"
      version = "~> 3.0"
    }
  }
  required_version = ">= 1.0.0"
}

provider "aws" {
  region = var.aws_region
  # Credentials can be set via environment variables or AWS profile
}

provider "bitbucket" {
  # OAuth authentication - ensure you have the OAuth token set
  # Either as environment variable BITBUCKET_OAUTH_TOKEN
  # or set in the provider configuration below
  oauth_token = var.bitbucket_oauth_token
}

# Define local variables for paths
locals {
  lambda_function_name = var.lambda_function_name
  temp_dir             = "${path.module}/tmp"
  zip_file_path        = "${local.temp_dir}/${local.lambda_function_name}.zip"
  source_dir           = "${local.temp_dir}/source"
}

# Resource to get code from Bitbucket using OAuth token
resource "null_resource" "clone_repo" {
  provisioner "local-exec" {
    command = <<-EOT
      mkdir -p ${local.temp_dir}
      rm -rf ${local.source_dir}
      mkdir -p ${local.source_dir}
      
      # Clone the repository using Git and OAuth token
      git clone --single-branch --branch ${var.bitbucket_branch} \
        https://x-token-auth:${var.bitbucket_oauth_token}@bitbucket.org/${var.bitbucket_workspace}/${var.bitbucket_repo}.git \
        ${local.source_dir}
        
      # Alternative: download using curl with OAuth token
      # curl -H "Authorization: Bearer ${var.bitbucket_oauth_token}" \
      #   -L https://api.bitbucket.org/2.0/repositories/${var.bitbucket_workspace}/${var.bitbucket_repo}/src/${var.bitbucket_branch}/ \
      #   -o ${local.temp_dir}/repo.zip
      # unzip -o ${local.temp_dir}/repo.zip -d ${local.source_dir}
      
      cd ${local.source_dir}
      pip install -r requirements.txt -t .
      zip -r ${local.zip_file_path} .
    EOT
  }

  # Triggers - rerun when any of these values change
  triggers = {
    repo_branch = var.bitbucket_branch
    time_stamp  = timestamp()  # Force update on each apply
  }
}

# Create an S3 bucket for Lambda code
resource "aws_s3_bucket" "lambda_bucket" {
  bucket = "${var.lambda_function_name}-code-${var.environment}"
}

resource "aws_s3_bucket_ownership_controls" "lambda_bucket_ownership" {
  bucket = aws_s3_bucket.lambda_bucket.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

resource "aws_s3_bucket_acl" "lambda_bucket_acl" {
  bucket = aws_s3_bucket.lambda_bucket.id
  acl    = "private"
  depends_on = [aws_s3_bucket_ownership_controls.lambda_bucket_ownership]
}

# Upload the Lambda code to S3
resource "aws_s3_object" "lambda_code" {
  bucket = aws_s3_bucket.lambda_bucket.id
  key    = "${local.lambda_function_name}.zip"
  source = local.zip_file_path
  etag   = filemd5(local.zip_file_path)

  depends_on = [null_resource.clone_repo]
}

# Create the Lambda IAM role
resource "aws_iam_role" "lambda_role" {
  name = "${var.lambda_function_name}-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

# Lambda basic execution policy attachment
resource "aws_iam_role_policy_attachment" "lambda_basic_execution" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# Create the Lambda function
resource "aws_lambda_function" "lambda_function" {
  function_name = local.lambda_function_name
  description   = "Lambda function deployed from Bitbucket repository"
  
  s3_bucket     = aws_s3_bucket.lambda_bucket.id
  s3_key        = aws_s3_object.lambda_code.key
  
  runtime       = "python3.9"
  handler       = var.lambda_handler
  timeout       = var.lambda_timeout
  memory_size   = var.lambda_memory_size
  
  role          = aws_iam_role.lambda_role.arn
  
  environment {
    variables = var.lambda_environment_variables
  }

  depends_on = [
    aws_s3_object.lambda_code,
    aws_iam_role_policy_attachment.lambda_basic_execution
  ]
}

# Output the Lambda function ARN
output "lambda_function_arn" {
  description = "The ARN of the Lambda function"
  value       = aws_lambda_function.lambda_function.arn
}

output "s3_bucket_name" {
  description = "Name of the S3 bucket storing the Lambda code"
  value       = aws_s3_bucket.lambda_bucket.bucket
}