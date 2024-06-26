from rest_framework import status

error_codes = {
    'INVALID_SIGNUP_MODE': {
        'key': 'invalid_signup_mode',
        'message': 'invalid signup mode',
        'status_code': status.HTTP_422_UNPROCESSABLE_ENTITY,
    },


    'USER_ALREADY_EXISTS': {
        'key': 'user_already_exists',
        'message': 'User with given email already exists',
        'status_code': status.HTTP_422_UNPROCESSABLE_ENTITY,
    },

    'BAD_REQUEST': {
        'key': 'bad_request',
        'message': 'Bad request, missing params',
        'status_code': status.HTTP_422_UNPROCESSABLE_ENTITY,
    },

    'OPERATION_FAILED': {
        'key': 'operation_failed',
        'message': 'Something went wrong due to invalid params',
        'status_code': status.HTTP_422_UNPROCESSABLE_ENTITY,
    },
}
