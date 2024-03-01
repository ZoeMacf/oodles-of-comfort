from django.db import models
from cloudinary.models import CloudinaryField
import uuid

# Create your models here.

class UserProfile(models.Model):
    """ Creates a model for the UserProfile"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, null=True, blank=True)
    user_img = CloudinaryField("image", default="placeholder")
    email = models.EmailField()
    commented_recipes = model.ManyToMany(Comment, related_name="commented_recipes")
    likes = model.ManyToMany(LikedRecipe, related_name="likes")
    date_joined = models.DateTimeField(auto_now_add=True)

class LikedRecipe(models.Model):
    """Creates a model for user likes on a recipe"""

    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="recipe_posts"
    )
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="recipe_likes"
    )
    liked_on = models.DateTimeField(auto_now_add=True)

