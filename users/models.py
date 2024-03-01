from django.db import models
import uuid

# Create your models here.

class UserProfile(models.Model):
    """ Creates a model for the UserProfile"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    date_joined = models.DateTimeField(auto_now_add=True)
    