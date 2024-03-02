from django.db import models
from cloudinary.models import CloudinaryField
# from blog.models import LikedRecipe
import uuid

# Create your models here.

class UserProfile(models.Model):
    """ Creates a model for the UserProfile"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, null=True, blank=True)
    user_img = CloudinaryField("image", default="placeholder")
    email = models.EmailField()
    # commented_recipes = models.ManyToManyField(Comment, related_name="commented_recipes")
    # likes = models.ManyToManyField(LikedRecipe, related_name="likes")
    date_joined = models.DateTimeField(auto_now_add=True)
    


