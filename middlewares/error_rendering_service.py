from rest_framework.response import Response


def error_json(error):
    error_key = error.get('key')
    error_message = error.get('message')
    status_code = error.get('status_code')
    return Response(
        {
            'key': error_key,
            'message': error_message,
        },
        status=status_code
    )

