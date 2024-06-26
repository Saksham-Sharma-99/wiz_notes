from ...models import User
from constants.error_codes import error_codes
from django.conf import settings
from external_apis.third_party_login.google import GoogleAuth
from constants.error_codes import error_codes


class CreateService:

    def __init__(self, data):
        self.data = data
        self.mode = data.get('mode')
        self.signup_data = data.get('signup_data')
        self.third_party_signup_mode = data.get('third_party_signup_mode')

    def signup(self):
        if self.mode == 'third_party_signup' and self.third_party_signup_mode == 'google':
            return self.__fetch_or_create_user_from_google_token()
        else:
            return None, error_codes['OPERATION_FAILED']


    def __fetch_or_create_user_from_google_token(self):
        token = self.signup_data.get('token')
        redirect_uri = self.data.get('redirect_uri')
        
        access_token, error = GoogleAuth().fetch_exchange_token(redirect_uri=redirect_uri, temp_code=token)
        if error is not None: return None, error

        email, error = GoogleAuth().fetch_user_information(access_token=access_token)
        print('email', email)
        if error is not None: return None, error

        user = User.objects.filter(email=email, status='active').first()
        if user:
            return user, None
        else:
            new_user = User.objects.create(email=email, name=email.split('@')[0], status='active')
            return new_user, None