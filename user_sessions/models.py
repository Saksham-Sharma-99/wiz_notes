from django.db import models
from users.models import User

# Create your models here.
class UserSession(models.Model):
    class Meta:
        db_table = 'user_sessions'

    class Status(models.TextChoices):
        ACTIVE = "active", "active"
        INACTIVE = "inactive", "inactive"

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sessions', db_column='user_id'
    )
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.ACTIVE)
    access_token = models.CharField(max_length=200, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.access_token
