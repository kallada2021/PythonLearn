# terraform.tfvars
# Fill in your specific values

aws_region              = "us-east-1"
environment             = "dev"
lambda_function_name    = "my-python-lambda"
lambda_handler          = "lambda_function.lambda_handler"
lambda_timeout          = 30
lambda_memory_size      = 256

bitbucket_oauth_token   = "your-bitbucket-oauth-token"  # OAuth token for Bitbucket API access
# bitbucket_ssh_key_path = "~/.ssh/id_rsa"  # Uncomment if using SSH authentication
bitbucket_workspace     = "your-workspace-name"  
bitbucket_repo          = "your-repo-name"
bitbucket_branch        = "main"

lambda_environment_variables = {
  ENV_VAR_1 = "value1",
  ENV_VAR_2 = "value2"
}