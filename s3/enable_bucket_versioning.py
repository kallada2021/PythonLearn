"""
Enables Bucket Versioning
"""

import boto3
import botocore


def enable_s3_versioning(bucket):
    """
    Enables bucket versioning

    Args:
        bucket_name str : name of the bucket
    """

    try:
        s3_resource = boto3.resource("s3")

        bucket_versioning = s3_resource.BucketVersioning(bucket)

        if bucket_versioning.status != "Enabled":
            response = bucket_versioning.enable()

            status_code = response["ResponseMetadata"]["HTTPStatusCode"]

            if status_code == 200:
                print(f"Version status is now {bucket_versioning.status} for {bucket}")
            else:
                print(f"Enabling versioning for bucket {bucket} failed status code {bucket_versioning.status_code}")
        else:
            print(f"Bucket Versioning is already enabled for {bucket_versioning.bucket_name}")
    except botocore.exceptions.ClientError as e:
        print(e.response["error"]["message"])
    except botocore.exceptions.ParamValidationError as e:
        print(e)
        

try:
    s3_name = input("Input bucket name ")
    enable_s3_versioning(s3_name)
except ValueError as value_error:
    print(value_error)
except KeyboardInterrupt:
    print("Exiting the script")
