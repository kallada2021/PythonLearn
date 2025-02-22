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