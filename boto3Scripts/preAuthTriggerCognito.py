import json
import logging
import os

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Lambda function for Cognito pre-authentication trigger.
    Validates that the user's assigned role from rules mapping matches the custom_cognito_role attribute.
    
    Args:
        event (dict): Event data from Cognito
        context (object): Lambda context
        
    Returns:
        dict: The modified event object
    """
    logger.info(f"Pre-authentication event: {json.dumps(event)}")
    
    try:
        # Extract user information from the event
        user_attributes = event.get('request', {}).get('userAttributes', {})
        username = event.get('userName')
        
        # Get the rule-mapped role (this depends on your specific Cognito setup)
        # You might need to modify this depending on how you're passing the role information
        rule_mapped_role = event.get('callerContext', {}).get('clientId')
        
        # Get the user's expected role from custom attributes
        custom_role = user_attributes.get('custom:cognito_role')
        
        logger.info(f"User: {username}, Rule-mapped role: {rule_mapped_role}, Custom role: {custom_role}")
        
        # Validate the role
        if custom_role and rule_mapped_role and custom_role != rule_mapped_role:
            logger.error(f"Role validation failed for user: {username}. " 
                         f"Expected role: {custom_role}, Actual role: {rule_mapped_role}")
            
            # Deny authentication
            raise Exception("Role validation failed. Authentication denied.")
        
        # If we get here, role validation passed
        logger.info(f"Role validation passed for user: {username}")
        
        # Return the event
        return event
        
    except Exception as e:
        logger.error(f"Error during pre-authentication: {str(e)}")
        raise Exception("Authentication error")
