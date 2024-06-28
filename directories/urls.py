from django.urls import path
from . import controllers

urlpatterns = [
    path("", controllers.directories, name="directories"),
    path("<str:ref_id>/", controllers.directory, name="directory"),
]
