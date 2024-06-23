from celery import shared_task
from .models import Document
from .services.text_extraction_service import process_document_and_extract_text

@shared_task
def process_document(document_id):
    # Retrieve the document
    document = Document.objects.get(id=document_id)

    # Perform the background processing (e.g., text extraction, analysis)
    # For example, let's just print the document title for now
    print(f'Processing document: {document.title}')

    text = process_document_and_extract_text(document)
    document.text_content = text

    # Update the document status to completed
    document.attached_docs_status = Document.AttachedDocStatus.COMPLETED
    document.save()