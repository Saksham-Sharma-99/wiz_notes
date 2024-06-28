from celery import shared_task
from users.models import User
from .models import Directory

@shared_task
def create_default_directory(user_id):
    print('creating default directory for', user_id)
    user = User.objects.get(id=user_id)
    Directory.objects.create(
        user=user,
        directory_type='default',
        title='Default',
        status='active'
    )
