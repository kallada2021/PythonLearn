"""
Puts an Object in an S3 Bucket
"""

import boto3
import botocore


def put_file_s3(bucket, filename, key):
    """
    Puts A File In An S3 Bucket
    Args:
        bucket str : Name of the bucket
        filename str : Path to the file
        key str : Name of the file in the S3 bucket
    """
    try:
        print(f"Putting {filename} into bucket {bucket}")
        s3_resource = boto3.resource("s3")
        s3_resource.Bucket(bucket).upload_file(
            filename,
            key,
            ExtraArgs={"ServerSideEncryption": "AES256", "Tagging": "Deployment=Boto3"},
        )

        print(f"File {key} has been created in bucket {bucket}")
    except botocore.exceptions.ClientError as e:
        print(e.response["error"]["message"])
    except botocore.exceptions.ParamValidationError as e:
        print(e)


def put_object_s3(bucket, body, key):
    """
    Puts An Object In An S3 Bucket
    """
    try:
        print(f"Putting {body} into bucket {bucket}")
        s3_resource = boto3.resource("s3")
        bucket = s3_resource.Bucket(bucket)

        bucket.put_object(
            Key=key,
            Body=body,
            ServerSideEncryption="AES256",
            Tagging="Deployment=Boto3",
        )

        print(f"File {key} has been created in bucket {bucket.name}")
    except botocore.exceptions.ClientError as e:
        print(e.response["error"]["message"])
    except botocore.exceptions.ParamValidationError as e:
        print(e)


try:
    s3 = input("Enter Bucket name ")
    contents = input("Enter the file ")
    name = input("Enter the file name")

    # put_object_s3(s3, contents, name)
    put_file_s3(s3, contents, name)
except ValueError as value_error:
    print(value_error)
