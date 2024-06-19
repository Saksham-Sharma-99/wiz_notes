from django.urls import path, include
from . import controllers

urlpatterns = [
    path("", controllers.upload_document, name="documents"),
]