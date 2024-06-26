from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from user_sessions.models import UserSession  # Assuming your sessions model is in 'sessions' app

user_exempted_routes = [
    '/users/signup/',
    '/users/login/'
]
other_exempted_routes = [
    '/favicon.ico'
]

class UserSessionAuthentication:
    EXEMPT_ROUTES = user_exempted_routes + other_exempted_routes

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)

        if any(request.path.startswith(route) for route in self.EXEMPT_ROUTES):
            return self.get_response(request)
        # Process the request before it reaches the view

        # Check if 'Authorization' header is present in the request
        authorization_header = request.headers.get('Authorization')
        if authorization_header:
            try:
                _, token = authorization_header.split()
                # Query active sessions with matching token
                try:
                    session = UserSession.objects.get(status=UserSession.Status.ACTIVE, access_token=token)
                    # Attach user to request if session found
                    request.user = session.user
                except ObjectDoesNotExist:
                    return JsonResponse({'error': 'Not authorized'}, status=401)
            except ValueError:
                return JsonResponse({'error': 'Invalid authorization header format'}, status=422)
        else:
            return JsonResponse({'error': 'Authorization header required'}, status=422)

        response = self.get_response(request)

        # Process the response before it's returned to the client

        return response
