import boto3
from django.conf import settings
from urllib.parse import urlparse


def extract_file_key(private_url):
    parsed_url = urlparse(private_url)
    # The path will be of the form /bucket_name/file_key, so we remove the leading '/'
    file_key = parsed_url.path.lstrip('/')
    return file_key    

def generate_presigned_url(private_url):
    file_key = extract_file_key(private_url)
    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION
    )

    # Generate a presigned URL valid for 7 days
    presigned_url = s3_client.generate_presigned_url(
        'get_object',
        Params={
            'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
            'Key': file_key
        },
        ExpiresIn=604800  # 7 days in seconds
    )

    return presigned_url
