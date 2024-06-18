from django.urls import path, include
from . import controllers

urlpatterns = [
    path("", controllers.health, name="health")
]