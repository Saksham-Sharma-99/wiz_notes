import boto3
import docx
import fitz  # PyMuPDF
import pandas as pd

from urllib.parse import urlparse
import os
from django.conf import settings
from .utils import extract_file_key
# from utils import e


def download_file_from_s3(s3_url, download_path):
    s3 = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION
    )
    parsed_url = urlparse(s3_url)
    bucket_name = parsed_url.netloc
    object_key = parsed_url.path.lstrip('/')

    # Construct a more clear download path
    file_name = os.path.basename(object_key)
    full_download_path = os.path.join(download_path, file_name)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(full_download_path), exist_ok=True)

    s3.download_file(bucket_name, object_key, full_download_path)
    return full_download_path

def extract_text_from_image(file_path):
    return ""

def extract_text_from_pdf(file_path):
    document = fitz.open(file_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

def extract_text_from_word(file_path):
    doc = docx.Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def extract_text_from_excel(file_path):
    excel_data = pd.read_excel(file_path, sheet_name=None)
    text = ""
    for sheet_name, sheet_data in excel_data.items():
        text += sheet_name + "\n"
        text += sheet_data.to_string(index=False)
        text += "\n"
    return text

def identify_file_type(file_path):
    # Get the file extension
    file_extension = os.path.splitext(file_path)[1].lower()

    # Mapping of file extensions to file types
    file_types = {
        '.pdf': 'pdf',
        '.doc': 'word_doc',
        '.docx': 'word_doc',
        '.xls': 'excel_or_csv',
        '.xlsx': 'excel_or_csv',
        '.csv': 'excel_or_csv',
        '.png': 'image',
        '.jpg': 'image',
        '.jpeg': 'image',
        '.gif': 'image',
        '.bmp': 'image',
        '.tiff': 'image',
    }

    # Return the identified file type
    return file_types.get(file_extension, 'other')

def extract_text(file_path):
    file_type = identify_file_type(file_path)

    if file_type == "pdf":
        text = extract_text_from_pdf(file_path)
    elif file_type == "word_doc":
        text = extract_text_from_word(file_path)
    elif file_type == "excel_or_csv":
        text = extract_text_from_excel(file_path)
    elif file_type == "image":
        text = extract_text_from_image(file_path)
    else:
        text = ""

    os.remove(file_path)
    return text


def process_document_and_extract_text(document):
    s3_url = document.private_url
    file_key = extract_file_key(document.private_url)
    s3_url = f's3://{settings.AWS_STORAGE_BUCKET_NAME}/{file_key}'

    download_path = f'{os.getcwd()}/tmp'
    full_download_path = download_file_from_s3(s3_url, download_path)

    return extract_text(full_download_path)
