from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class UserProfile(models.Model):
    """ Creates a model for the UserProfile"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, null=True, blank=True)
    user_img = CloudinaryField("image", default="placeholder")
    email = models.EmailField()
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}"
