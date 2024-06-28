from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = 'users'

    class Status(models.TextChoices):
        ACTIVE = "active", "active"
        INACTIVE = "inactive", "inactive"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.ACTIVE)
    last_login = models.DateTimeField(default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_active(self):
        return self.status == "active"

    def __str__(self):
        return self.name
