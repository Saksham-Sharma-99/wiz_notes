from ..models import Document
from ..tasks import process_document
import os

def create_document(user, s3_url, title, file):
    extension_type = os.path.splitext(file.name)[1][1:]
    document = Document.objects.create(
        user=user,
        private_url=s3_url,
        title=title,
        extension_type=extension_type
    )
    
    # Trigger the Celery task
    process_document.delay(document.id)
    
    return document
