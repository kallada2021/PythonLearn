import json
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Pre-authentication Lambda trigger for Amazon Cognito.
    Validates if the user's role from rules mapping matches their custom_cognito_role attribute.
    
    Args:
        event (dict): The event data from Cognito
        context (LambdaContext): AWS Lambda context
        
    Returns:
        dict: The event object, unmodified if validation passes
        
    Raises:
        Exception: If validation fails, preventing authentication
    """
    logger.info(f"Pre-authentication event received: {json.dumps(event)}")
    
    try:
        # Extract user information from the event
        user_attributes = event.get('request', {}).get('userAttributes', {})
        username = event.get('userName')
        
        # Get user's custom role attribute
        custom_role = user_attributes.get('custom:cognito_role')
        
        # Get the mapped role from the client context or user pool rules
        # Note: The exact path to the mapped role may vary based on your Cognito setup
        # You may need to adjust this to match your specific implementation
        client_id = event.get('callerContext', {}).get('clientId')
        
        # Get the role mapping for this client
        # In a real implementation, you might query a database or SSM Parameter Store
        # to get the role mapping for this client ID
        mapped_role = get_mapped_role_for_client(client_id)
        
        logger.info(f"User: {username}, Custom role: {custom_role}, Mapped role: {mapped_role}")
        
        # Perform role validation
        if custom_role and mapped_role and custom_role != mapped_role:
            logger.error(f"Role mismatch for user {username}. Expected: {custom_role}, Got: {mapped_role}")
            
            # You could add additional preparatory actions here before denying auth
            # For example: log to CloudWatch, send metrics to CloudWatch, notify admins, etc.
            
            # Deny authentication by raising an exception
            raise Exception(f"Role validation failed: User role '{custom_role}' does not match required role '{mapped_role}'")
        
        # If we reach here, validation passed
        logger.info(f"Role validation passed for user: {username}")
        return event
        
    except Exception as e:
        logger.error(f"Error in pre-authentication validation: {str(e)}")
        raise Exception("Authentication denied due to validation failure")

def get_mapped_role_for_client(client_id):
    """
    Retrieves the mapped role for a specific client ID.
    
    Args:
        client_id (str): The Cognito client ID
        
    Returns:
        str: The mapped role for the client
    """
    # Hardcoded role mappings - replace with your actual role assignments
    # Real Cognito client IDs are typically 26 characters long and alphanumeric
    role_mappings = {
        # Example client IDs as you would see in Cognito
        "1abc2defghijklmnopqrstuv3": "admin",
        "2def3ghijklmnopqrstuvwxyz4": "user",
        "3ghi4jklmnopqrstuvwxyzabc5": "readonly",
        "4jkl5mnopqrstuvwxyzabcdef6": "developer",
        "5mno6pqrstuvwxyzabcdefghi7": "tester"
    }
    
    # Return the mapped role or None if client ID not found
    mapped_role = role_mappings.get(client_id)
    
    if not mapped_role:
        logger.warning(f"No role mapping found for client ID: {client_id}")
        
    return mapped_role
EXample Event
{
  "version": "1",
  "region": "us-east-1",
  "userPoolId": "us-east-1_aBcDeFgHi",
  "userName": "test-user",
  "callerContext": {
    "awsSdkVersion": "aws-sdk-js-2.6.4",
    "clientId": "1abc2defghijklmnopqrstuv3"
  },
  "triggerSource": "PreAuthentication_Authentication",
  "request": {
    "userAttributes": {
      "sub": "11111111-2222-3333-4444-555555555555",
      "email_verified": "true",
      "custom:cognito_role": "admin",
      "phone_number_verified": "true",
      "phone_number": "+12065551234",
      "email": "user@example.com"
    },
    "userNotFound": false
  },
  "response": {}
}
