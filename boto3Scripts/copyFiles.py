# Run: python s3_copy_job_runner.py path/to/your/control_file.json

import json
import os
import time
import hashlib
import boto3
from botocore.exceptions import ClientError

def compute_md5(file_path):
    """Compute MD5 hash of a local file and return as Base64 string."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.digest(), hash_md5.hexdigest()

def object_exists(s3_client, bucket, key):
    """Check if an object exists in S3."""
    try:
        s3_client.head_object(Bucket=bucket, Key=key)
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            return False
        raise

def copy_object(job, global_options):
    """Execute a single copy job."""
    s3_dest = boto3.client('s3', region_name=job['destination']['region'])
    job_options = job.get('options', {})
    overwrite = job_options.get('overwrite', True)
    source_type = job['source']['type']

    # Skip if object exists and overwrite is disabled
    if not overwrite and object_exists(s3_dest, job['destination']['bucket'], job['destination']['key']):
        print(f"Skipping existing object: s3://{job['destination']['bucket']}/{job['destination']['key']}")
        return

    # Handle Local → S3 copy
    if source_type == 'local':
        local_path = job['source']['path']
        extra_args = {
            'Metadata': job_options.get('metadata', {}),
            'StorageClass': job_options.get('storageClass', 'STANDARD'),
            'ACL': job_options.get('acl', 'private')
        }

        # Add Object Lock headers if specified
        if 'objectLock' in job_options:
            extra_args['ObjectLockMode'] = job_options['objectLock']['mode']
            extra_args['ObjectLockRetainUntilDate'] = job_options['objectLock']['retainUntil']
            if job_options['objectLock'].get('legalHold', False):
                extra_args['ObjectLockLegalHoldStatus'] = 'ON'

        # Upload with MD5 verification
        md5_digest, md5_hex = compute_md5(local_path)
        s3_dest.upload_file(
            local_path,
            job['destination']['bucket'],
            job['destination']['key'],
            ExtraArgs=extra_args
        )

        # Verify checksum
        if job_options.get('checksum', {}).get('verify', False):
            etag = s3_dest.head_object(
                Bucket=job['destination']['bucket'],
                Key=job['destination']['key']
            )['ETag'].strip('"')
            assert etag == md5_hex, "MD5 checksum mismatch!"

    # Handle S3 → S3 copy
    elif source_type == 's3':
        source_bucket = job['source']['bucket']
        source_key = job['source']['key']
        copy_source = {'Bucket': source_bucket, 'Key': source_key}

        s3_dest.copy_object(
            Bucket=job['destination']['bucket'],
            Key=job['destination']['key'],
            CopySource=copy_source,
            StorageClass=job_options.get('storageClass', 'STANDARD'),
            MetadataDirective='REPLACE' if job_options.get('metadata') else 'COPY',
            **({'Metadata': job_options['metadata']} if job_options.get('metadata') else {})
        )

def main(control_file_path):
    with open(control_file_path) as f:
        config = json.load(f)

    for idx, job in enumerate(config['jobs']):
        print(f"Processing job {idx+1}/{len(config['jobs'])}")
        
        retry_config = job.get('errorHandling', {}).get('retry', {})
        max_attempts = retry_config.get('maxAttempts', 1)
        backoff = retry_config.get('backoffMultiplier', 1)

        for attempt in range(1, max_attempts + 1):
            try:
                copy_object(job, config['globalOptions'])
                break
            except Exception as e:
                if attempt == max_attempts:
                    if config['globalOptions'].get('onFailure', 'continue') == 'abort':
                        raise
                    print(f"Job failed after {max_attempts} attempts: {str(e)}")
                else:
                    sleep_time = attempt * backoff
                    print(f"Attempt {attempt} failed. Retrying in {sleep_time}s...")
                    time.sleep(sleep_time)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("control_file", help="Path to JSON control file")
    args = parser.parse_args()
    
    main(args.control_file)
