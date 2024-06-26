from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers.user_profile_serializer import UserProfileSerializer
from .serializers.user_auth_serializer import UserLoginSerializer
from .services.signup.validate_service import ValidateService
from .services.signup.create_service import CreateService
from middlewares.error_rendering_service import error_json
from user_sessions.services.create_service import create_session

# Create your views here.
@api_view(['GET'])
def profile(request):
    user = request.user
    serializer = UserProfileSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def signup(request):
    validate_service = ValidateService(data=request.data)
    error = validate_service.validate()
    if error is not None: return error_json(error)

    signup_service = CreateService(data=request.data)
    user, error = signup_service.signup()
    if error is not None: return error_json(error)

    create_session(user)
    serializer = UserLoginSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def login(request):
    mode = request.data.get('mode', None)
    login_data = request.data.get('login_data', None)