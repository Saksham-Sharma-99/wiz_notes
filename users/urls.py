from django.urls import path, include
from . import controllers

urlpatterns = [
    path("open/", controllers.health, name="health"),
    path("closed/", controllers.health, name="health")
]