from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DirectorySerializer
from .models import Directory
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def directories(request):
    if request.method == 'GET':
        return get_directories(request)
    elif request.method == 'POST':
        return post_directories(request)

def get_directories(request):
    directories_data = Directory.objects.filter(user=request.user, status='active')
    serializer = DirectorySerializer(directories_data, many=True)
    return Response(serializer.data)

def post_directories(request):
    serializer = DirectorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET', 'PATCH'])
def directory(request, ref_id):
    if request.method == 'GET':
        return get_directory(request, ref_id)
    elif request.method == 'PATCH':
        return update_directory(request, ref_id)


def get_directory(request, ref_id):
    directory_data = get_object_or_404(Directory, ref_id=ref_id, user=request.user, status='active')
    serializer = DirectorySerializer(directory_data)
    return Response(serializer.data)

def update_directory(request, ref_id):
    directory_data = get_object_or_404(Directory, ref_id=ref_id, user=request.user)
    if request.data.get('status') == 'inactive':
        directory_data.status = 'inactive'
        directory_data.save()
        return Response(status=204)
    serializer = DirectorySerializer(directory_data, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)
