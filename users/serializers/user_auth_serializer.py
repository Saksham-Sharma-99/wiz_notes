from rest_framework import serializers
from ..models import User

class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['name', 'email', 'last_login', 'token']

    def get_token(self, obj):
        active_session = obj.sessions.filter(status='active').first()
        if active_session:
            return active_session.access_token
        return None
