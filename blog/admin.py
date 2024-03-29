from django.contrib import admin
from .models import Comment, Recipe, RecipeTag
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin):

    list_display = ("title", "slug", "status")
    search_fields = ["title"]
    list_filter = ("status",)
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("ingredients", "recipe_steps", "recipe_blurb")


# Register your models here.

admin.site.register(Comment)
admin.site.register(RecipeTag)
