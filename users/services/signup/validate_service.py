from ...models import User
from constants.error_codes import error_codes

class ValidateService:
    __allowed_modes = ['email_password', 'third_party_signup']
    __allowed_third_party_signup_modes = ['google']

    def __init__(self, data):
        self.data = data

    def validate(self):
        if self.data is None: return error_codes['BAD_REQUEST']

        signup_data = self.data.get('signup_data')
        mode = self.data.get('mode')
        third_party_signup_mode = self.data.get('third_party_signup_mode')

        if signup_data is None or mode is None: return error_codes['BAD_REQUEST']

        if mode not in self.__allowed_modes:
            return error_codes['INVALID_SIGNUP_MODE']
        elif mode == 'third_party_signup':
            token = signup_data.get('token', None)
            redirect_uri = self.data.get('redirect_uri')
            return self.__validate_third_party_signup(third_party_signup_mode, token, redirect_uri)
        elif mode == 'email_password':
            password = signup_data.get('password', None)
            email = signup_data.get('email', None)
            return self.__email_password_signup(email, password)
        else:
            return error_codes['BAD_REQUEST']

    def __validate_third_party_signup(self, third_party_signup_mode, token, redirect_uri):
        if token is None or redirect_uri is None: return error_codes['BAD_REQUEST']
        if third_party_signup_mode not in self.__allowed_third_party_signup_modes: return error_codes['INVALID_SIGNUP_MODE']

        return None

    @staticmethod
    def __email_password_signup(email, password):
        if email is None or password is None: return error_codes['BAD_REQUEST']

        user_exists = User.objects.filter(email=email).exists()
        if user_exists: return error_codes['USER_ALREADY_EXISTS']

        return None
