# Script Features
Retry Logic: Implements exponential backoff for failed operations

Checksum Verification: Validates MD5 for local→S3 transfers

Object Lock Support: Applies retention policies if specified

Dry Run Support: Add "dryRun": true in globalOptions to test without modifying data

Cross-Region Copies: Handles S3→S3 transfers across regions

Key Fields Explained in JSON CTRL File
Field	Description
jobs[]	Array of copy operations to execute.
source.type	local (filesystem) or s3 (existing S3 object).
destination	Target S3 bucket/key and region.
options	Copy behavior: ACLs, storage class, Object Lock, metadata, overwrite rules.
objectLock	Applies retention rules (if the destination bucket has Object Lock enabled).
checksum	Verify data integrity using MD5/SHA256.
errorHandling	Retry logic and failure behavior (continue or abort).
globalOptions	Settings for the entire batch (logging, dry runs, notifications).

Example Use Cases
Local → S3 Copy

Copies a local file to S3 with Object Lock and metadata.

Verifies the MD5 checksum after upload.

Retries failed uploads up to 3 times.

S3 → S3 Copy

Copies an object between buckets across regions.

Transitions the storage class to Glacier.

Skips if the destination object already exists ("overwrite": false).

Ctr1.json file explained
Explanation of the Template:
Top-Level Structure:
"copy_operations": An array of individual copy tasks.
"global_settings": Optional settings applied to all operations (e.g., dry run, concurrency limits).
Copy Operation Fields:
"source": Defines the S3 bucket, key (path), and optional version ID of the object to copy.
"destination": Specifies the target bucket and key.
"metadata": Controls metadata handling:
"user-defined": Custom key-value pairs.
"directive": COPY reuses source metadata; REPLACE applies new metadata.
"optional_parameters": Configures additional S3 features:
"storage_class": Sets the storage tier (e.g., STANDARD, GLACIER).
"acl": Applies an access control policy.
"object_lock": Configures Object Lock for compliance/governance.
"tagging": Adds key-value tags.
"encryption": Specifies server-side encryption type.
"content_type": Overrides the MIME type.
"cache_control": Sets caching headers.
Global Settings:
"dry_run": Simulates operations for testing.
"overwrite": Controls whether to replace existing objects.
"max_concurrent_copies": Limits parallelism for resource management.
"retry_attempts" and "retry_delay_seconds": Handles transient failures.

PreAuthTriggerLambda for Cognito
How to Use This Lambda Trigger

Deploy this Lambda function to your AWS account with the appropriate IAM permissions.
Configure the function as a Cognito Pre-Authentication trigger in your AWS Cognito User Pool.
Ensure your user attributes include a custom attribute named custom:cognito_role that stores the expected role for each user.

This function works by:

Extracting user attributes from the Cognito event data
Getting the role information from the rules mapping (in this example via clientId - you may need to adjust this based on how your role information is being passed)
Comparing the mapped role with the custom role attribute stored in the user's profile
Either allowing the authentication to proceed if the roles match, or throwing an exception to deny authentication if they don't match

You can extend this code to perform additional preparatory actions before authentication, such as:

Logging authentication attempts
Checking user status in other systems
Updating user metadata
Implementing custom rate limiting
Validating additional attributes