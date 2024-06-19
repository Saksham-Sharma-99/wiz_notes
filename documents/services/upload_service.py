import boto3
from django.conf import settings
import uuid

def upload_to_s3(file, user):
    print(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY, settings.AWS_REGION)
    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION
    )

    file_extension = file.name.split('.')[-1]
    file_key = f"{user.id}/{uuid.uuid4()}.{file_extension}"

    s3_client.upload_fileobj(
        file,
        settings.AWS_STORAGE_BUCKET_NAME,
        file_key,
        # ExtraArgs={'ACL': 'private'}
    )

    s3_url = f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.{settings.AWS_REGION}.amazonaws.com/{file_key}"
    return s3_url
