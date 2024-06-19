from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Document
from .services.upload_service import upload_to_s3
from .services.create_service import create_document
import os

@csrf_exempt
@api_view(['POST'])
def upload_document(request):
    user = request.user
    file = request.FILES.get('file')
    title = request.data.get('title')

    if not file:
        return Response({'error': 'No file provided'}, status=422)
    if not title:
        return Response({'error': 'No title provided'}, status=422)

   # Upload file to S3
    s3_url = upload_to_s3(file, user)

    # Create a new Document instance using the service
    document = create_document(user=user, s3_url=s3_url, title=title, file=file)


    return Response({'message': 'File uploaded successfully', 'document_id': document.title})
