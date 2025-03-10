import pytest
import json
from unittest.mock import patch, MagicMock
import logging

# Import the Lambda function
# Assuming your Lambda function is in a file called lambda_function.py
# If it's in a different file, adjust the import accordingly
import lambda_function

# Test fixtures to be reused across tests
@pytest.fixture
def base_event():
    """Base event fixture with standard structure."""
    return {
        "version": "1",
        "region": "us-east-1",
        "userPoolId": "us-east-1_aBcDeFgHi",
        "userName": "test-user",
        "callerContext": {
            "awsSdkVersion": "aws-sdk-js-2.6.4",
            "clientId": "1abc2defghijklmnopqrstuv3"  # Maps to "admin" role
        },
        "triggerSource": "PreAuthentication_Authentication",
        "request": {
            "userAttributes": {
                "sub": "11111111-2222-3333-4444-555555555555",
                "email_verified": "true",
                "cog_role": "custom_cognito_role",
                "custom_cognito_role": "admin",
                "custom:sid": "B78906",
                "email": "user@example.com"
            },
            "userNotFound": False
        },
        "response": {}
    }

@pytest.fixture(autouse=True)
def disable_logging():
    """Disable logging for all tests."""
    logging.disable(logging.CRITICAL)
    yield
    logging.disable(logging.NOTSET)


def test_success_matching_roles(base_event):
    """Test successful authentication when roles match."""
    # Use the base event which has matching roles (admin)
    result = lambda_function.lambda_handler(base_event, {})
    
    # Verify the result is the event (authentication allowed)
    assert result == base_event


def test_failure_mismatched_roles(base_event):
    """Test failed authentication when roles don't match."""
    # Modify the event to have mismatched roles
    base_event["request"]["userAttributes"]["custom_cognito_role"] = "user"  # doesn't match "admin" role
    
    # Authentication should be denied
    with pytest.raises(Exception) as excinfo:
        lambda_function.lambda_handler(base_event, {})
    
    # Verify the error message
    assert "Role validation failed" in str(excinfo.value)


def test_failure_missing_custom_role(base_event):
    """Test failed authentication when custom role is missing."""
    # Remove the role attributes
    del base_event["request"]["userAttributes"]["cog_role"]
    del base_event["request"]["userAttributes"]["custom_cognito_role"]
    
    # Authentication should be denied
    with pytest.raises(Exception) as excinfo:
        lambda_function.lambda_handler(base_event, {})
    
    # Verify the error message
    assert "Incomplete role information" in str(excinfo.value)


def test_failure_missing_mapped_role(base_event):
    """Test failed authentication when mapped role is missing (unknown client ID)."""
    # Set an unknown client ID
    base_event["callerContext"]["clientId"] = "unknown-client-id"
    
    # Authentication should be denied
    with pytest.raises(Exception) as excinfo:
        lambda_function.lambda_handler(base_event, {})
    
    # Verify the error message
    assert "Incomplete role information" in str(excinfo.value)


def test_custom_sid_as_username():
    """Test that custom:sid is used when username is missing."""
    # Create an event with missing username
    event = {
        "version": "1",
        "region": "us-east-1",
        "userPoolId": "us-east-1_aBcDeFgHi",
        # Missing userName intentionally
        "callerContext": {
            "awsSdkVersion": "aws-sdk-js-2.6.4",
            "clientId": "1abc2defghijklmnopqrstuv3"
        },
        "triggerSource": "PreAuthentication_Authentication",
        "request": {
            "userAttributes": {
                "sub": "11111111-2222-3333-4444-555555555555",
                "email_verified": "true",
                "cog_role": "custom_cognito_role",
                "custom_cognito_role": "admin",
                "custom:sid": "B78906",
                "email": "user@example.com"
            },
            "userNotFound": False
        },
        "response": {}
    }
    
    # Patch the logging.info function to capture log messages
    with patch('logging.info') as mock_log_info:
        # Call the lambda handler
        lambda_function.lambda_handler(event, {})
        
        # Check if the custom:sid was used as username
        sid_as_username_logged = any(
            "Using custom:sid as username: B78906" in str(call) 
            for call in mock_log_info.call_args_list
        )
        assert sid_as_username_logged, "custom:sid should be used as username"


def test_different_client_id_role_mapping(base_event):
    """Test authentication with a different client ID."""
    # Modify the event to use a different client ID and matching role
    base_event["callerContext"]["clientId"] = "2def3ghijklmnopqrstuvwxyz4"  # Maps to "user" role
    base_event["request"]["userAttributes"]["custom_cognito_role"] = "user"
    
    # Call the lambda handler
    result = lambda_function.lambda_handler(base_event, {})
    
    # Verify the result is the event (authentication allowed)
    assert result == base_event


def test_malformed_event():
    """Test handling of a malformed event."""
    # Create a completely malformed event
    event = {
        "malformed": "event"
    }
    
    # Should still handle the error gracefully
    with pytest.raises(Exception) as excinfo:
        lambda_function.lambda_handler(event, {})
    
    # Check that it's the expected error
    assert "Authentication denied" in str(excinfo.value)


def test_exception_in_role_retrieval(base_event, monkeypatch):
    """Test handling of exceptions during role retrieval."""
    # Define a mock function that raises an exception
    def mock_get_mapped_role(*args, **kwargs):
        raise Exception("Simulated error in role mapping retrieval")
    
    # Apply the mock to the get_mapped_role_for_client function
    monkeypatch.setattr(lambda_function, "get_mapped_role_for_client", mock_get_mapped_role)
    
    # Should handle the exception and deny authentication
    with pytest.raises(Exception) as excinfo:
        lambda_function.lambda_handler(base_event, {})
    
    # Check that it's the expected error
    assert "Authentication denied" in str(excinfo.value)


def test_null_event():
    """Test handling of a null event."""
    # Should handle gracefully
    with pytest.raises(Exception) as excinfo:
        lambda_function.lambda_handler(None, {})
    
    # Check that it's the expected error
    assert "Authentication denied" in str(excinfo.value)