from constants.error_codes import error_codes  # Adjust the import path as per your project structure
from ..models import UserSession  # Adjust the import path as per your project structure
from django.utils import timezone
import secrets  # for generating secure tokens

def generate_random_hex_token():
    return secrets.token_hex(16)  # Generates a random hexadecimal token of 16 bytes

def create_session(user):
    active_session = UserSession.objects.filter(user=user, status='active').first()
    if active_session:
        return active_session  # Return active session if exists

    random_hex_token = generate_random_hex_token()
    new_session = UserSession.objects.create(status='active', user=user, access_token=random_hex_token)
    user.last_login = timezone.now()
    user.save()
    return new_session  # Return newly created session
