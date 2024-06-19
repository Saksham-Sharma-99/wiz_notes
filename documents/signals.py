from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Document

@receiver(post_save, sender=Document)
def set_red_id(sender, instance, created, **kwargs):
    if created:
        count = Document.objects.filter(user_id=instance.user.id, status__in=["active", "deleted"]).count()
        instance.red_id = f"doc-{count}"
        instance.save()
