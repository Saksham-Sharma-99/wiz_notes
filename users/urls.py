from django.urls import path, include
from . import controllers

urlpatterns = [
    path("profile/", controllers.profile, name="profile"),
    path("signup/", controllers.signup, name="signup"),
    path("login/", controllers.login, name="login"),
]