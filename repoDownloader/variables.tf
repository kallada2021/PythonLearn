# variables.tf

variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Environment (dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "lambda_function_name" {
  description = "Name of the Lambda function"
  type        = string
}

variable "lambda_handler" {
  description = "Lambda function handler (e.g., 'lambda_function.lambda_handler')"
  type        = string
  default     = "lambda_function.lambda_handler"
}

variable "lambda_timeout" {
  description = "Lambda function timeout in seconds"
  type        = number
  default     = 30
}

variable "lambda_memory_size" {
  description = "Lambda function memory size in MB"
  type        = number
  default     = 128
}

variable "lambda_environment_variables" {
  description = "Environment variables for the Lambda function"
  type        = map(string)
  default     = {}
}

variable "bitbucket_oauth_token" {
  description = "Bitbucket OAuth token for repository access"
  type        = string
  sensitive   = true
}

# Alternative authentication method using SSH (if needed)
variable "bitbucket_ssh_key_path" {
  description = "Path to SSH private key for Bitbucket authentication"
  type        = string
  default     = "~/.ssh/id_rsa"
  sensitive   = true
}

variable "bitbucket_workspace" {
  description = "Bitbucket workspace/team name"
  type        = string
}

variable "bitbucket_repo" {
  description = "Bitbucket repository name"
  type        = string
}

variable "bitbucket_branch" {
  description = "Bitbucket branch to deploy"
  type        = string
  default     = "main"
}