"""
    Lists S3 Buckets 
"""

import boto3
import botocore


def list_buckets():
    """
    Lists S3 Buckets That exist in the Account
    """
    try:
        s3_resource = boto3.resource("s3")

        bucket_list = s3_resource.buckets.all()

        print("List of S3 Buckets")

        for bucket in bucket_list:
            print(f"{bucket.name}\t{bucket.creation_date}")
    except botocore.exceptions.ClientError as e:
        print(e.response["error"]["message"])
    except botocore.exceptions.ParamValidationError as e:
        print(e)


list_buckets()
