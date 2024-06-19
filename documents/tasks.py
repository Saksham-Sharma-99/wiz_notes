from celery import shared_task
from .models import Document

@shared_task
def process_document(document_id):
    # Retrieve the document
    document = Document.objects.get(id=document_id)

    # Perform the background processing (e.g., text extraction, analysis)
    # For example, let's just print the document title for now
    print(f'Processing document: {document.title}')

    # Update the document status to completed
    document.attached_docs_status = Document.AttachedDocStatus.COMPLETED
    document.save()
