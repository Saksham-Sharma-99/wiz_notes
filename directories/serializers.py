from rest_framework import serializers
from .models import Directory

class DirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Directory
        fields = ['ref_id', 'status', 'directory_type', 'title']
        read_only_fields = ['id', 'user']
