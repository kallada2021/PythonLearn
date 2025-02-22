# Script Features
Retry Logic: Implements exponential backoff for failed operations

Checksum Verification: Validates MD5 for local→S3 transfers

Object Lock Support: Applies retention policies if specified

Dry Run Support: Add "dryRun": true in globalOptions to test without modifying data

Cross-Region Copies: Handles S3→S3 transfers across regions

