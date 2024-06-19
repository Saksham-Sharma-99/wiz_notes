from django.db import models
from users.models import User

# Create your models here.
class Document(models.Model):
    class Meta:
        db_table = 'documents'

    class Status(models.TextChoices):
        ACTIVE = "active", "active"
        INACTIVE = "inactive", "inactive"
        DELETED = "deleted", "deleted"

    class AttachedDocStatus(models.TextChoices):
        UPLOADING = "uploading", "uploading"
        COMPLETED = "completed", "completed"
    
    class DocumentType(models.TextChoices):
        USER_INPUT = "user_input", "user_input"
        GENERATED_OUTPUT = "generated_output", "generated_output"
        DOCUMENT_ATTACHMENT = "document_attachment", "document_attachment"

    red_id = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.ACTIVE)
    attached_docs_status = models.CharField(
        max_length=50, choices=AttachedDocStatus.choices, default=AttachedDocStatus.UPLOADING
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='documents', db_column='user_id'
    )
    private_url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    extension_type = models.CharField(max_length=10)
    document_type = models.CharField(
        max_length=50, choices=DocumentType.choices, default=DocumentType.USER_INPUT
    )
    text_content = models.TextField(null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', db_column='parent_id', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_active(self):
        return self.status == "active"

    def __str__(self):
        return self.name
