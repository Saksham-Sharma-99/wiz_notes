from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import AnonymousUser

# Create your views here.
@api_view(['GET'])
def health(request):
    user = request.user
    if isinstance(user, AnonymousUser):
        return Response({ "status" : "Healthy" })
    else:
        return Response({ "status" : "Healthy", "user_name": user.name })
    