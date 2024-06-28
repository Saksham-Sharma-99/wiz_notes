from django.db import models
from users.models import User

class Directory(models.Model):
    class Meta:
        db_table = 'directories'

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    TYPE_CHOICES = [
        ('custom', 'Custom'),
        ('default', 'Default'),
    ]

    id = models.AutoField(primary_key=True)
    ref_id = models.CharField(max_length=100, unique=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    directory_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    title = models.CharField(max_length=255)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='directories', db_column='user_id'
    )

    def save(self, *args, **kwargs):
        if not self.ref_id:
            total_active_custom_directories = Directory.objects.filter(
                user=self.user, directory_type='custom', status='active'
            ).count()
            self.ref_id = f"dir-{total_active_custom_directories+1}"
        super().save(*args, **kwargs)
