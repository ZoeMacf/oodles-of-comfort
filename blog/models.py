from django.db import models
from users import UserProfile, LikedRecipe
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="recipe_posts"
    )
    prep_time = models.CharField(max_length=30, unique=False)
    cook_time = models.CharField(max_length=30, unique=False)
    ingredients = models.TextField()
    recipe_steps = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField("image", default="placeholder")
    recipe_blurb = models.TextField()
    recipe_likes = models.ForeignKey(LikedRecipe, related_name="recipe_likes")

class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
