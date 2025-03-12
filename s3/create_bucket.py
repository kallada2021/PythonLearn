"""
    Creates An S3 Bucket
"""

import boto3
import botocore


def create_bucket(bucket_name, region):
    """
    Creates An S3 Bucket and returns the name of the created bucket

    Args:
        bucket_name str : name of the bucket
        aws_region str: AWS Region
    """

    try:
        s3_resource = boto3.resource("s3")

        if region == "":
            bucket = s3_resource.create_bucket(Bucket=bucket_name)
        else:
            bucket = s3_resource.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={"LocationConstraint": region},
            )

        bucket.wait_until_exists()

        print(f"S3 Bucket {bucket.name} has been successfully created.")
    except botocore.exceptions.ClientError as e:
        print(e.response["error"]["message"])
    except botocore.exceptions.ParamValidationError as e:
        print(e)


try:
    s3 = "test-boto3-scripts-bucket"
    region = ""  # defaults to us-east-1
    create_bucket(s3, region)
except ValueError as value_error:
    print(value_error)
