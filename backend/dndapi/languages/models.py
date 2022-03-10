import uuid
from django.db import models

# Create your models here.
class Language(models.Model):
    language_uuid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name