# This template is flexible and can be extended based on specific needs (e.g., adding checksum validation or lifecycle rules). Let me know if you'd like to refine it further!
import json
import boto3

s3_client = boto3.client('s3')

with open('s3_copy_control.json', 'r') as f:
    config = json.load(f)

for operation in config['copy_operations']:
    source = operation['source']
    dest = operation['destination']
    params = operation.get('optional_parameters', {})
    
    copy_source = {'Bucket': source['bucket'], 'Key': source['key']}
    if 'version_id' in source:
        copy_source['VersionId'] = source['version_id']
    
    extra_args = {
        'StorageClass': params.get('storage_class', 'STANDARD'),
        'MetadataDirective': operation['metadata']['directive'],
        'Metadata': operation['metadata']['user-defined']
    }
    
    if 'acl' in params:
        extra_args['ACL'] = params['acl']
    
    s3_client.copy_object(
        CopySource=copy_source,
        Bucket=dest['bucket'],
        Key=dest['key'],
        **extra_args
    )