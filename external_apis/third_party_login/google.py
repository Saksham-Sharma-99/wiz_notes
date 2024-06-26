import requests
import json
from urllib.parse import urljoin
from django.conf import settings
from constants.error_codes import error_codes

class GoogleAuth:
    CLIENT_SECRET = settings.GOOGLE_AUTH_CLIENT_SECRET
    CLIENT_ID = settings.GOOGLE_AUTH_CLIENT_ID
    BASE_URL = "https://www.googleapis.com/oauth2/"
    ROUTES = {
        'v4_token': "v4/token",
        'v3_tokeninfo': "v3/tokeninfo",
    }

    @staticmethod
    def fetch_user_information(access_token):
        url = urljoin(GoogleAuth.BASE_URL, GoogleAuth.ROUTES['v3_tokeninfo'])
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {access_token}"
        }

        response = requests.post(url, headers=headers)
        response_body = response.json()

        print(response_body)
        if response.status_code != 200 or 'email' not in response_body:
            return None, error_codes['OPERATION_FAILED']

        return response_body['email'], None

    @staticmethod
    def fetch_exchange_token(redirect_uri, temp_code):
        url = urljoin(GoogleAuth.BASE_URL, GoogleAuth.ROUTES['v4_token'])
        headers = {
            'Content-Type': 'application/json',
        }
        body = {
            "client_id": GoogleAuth.CLIENT_ID,
            "client_secret": GoogleAuth.CLIENT_SECRET,
            "grant_type": "authorization_code",
            "redirect_uri": redirect_uri,
            "code": temp_code,
        }

        response = requests.post(url, headers=headers, json=body)
        response_body = response.json()

        print(response_body)
        if response.status_code != 200 or 'access_token' not in response_body:
            return None, error_codes['OPERATION_FAILED']

        return response_body['access_token'], None
