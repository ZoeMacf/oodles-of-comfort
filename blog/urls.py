from . import views
from django.urls import path

urlpatterns = [
    path("", views.RandomRecipes, name="home"),
    path("<slug:slug>/", views.recipe_detail, name="recipe_detail"),
    path("recipes", views.RecipeList.as_view(), name="recipe_list"),
    path("recipe_search", views.recipe_search, name="recipe_search"),
    path(
        "<slug:slug>/edit_comment/<int:comment_id>",
        views.edit_comment,
        name="edit_comment",
    ),
    path(
        "<slug:slug>/delete_comment/<int:comment_id>",
        views.comment_delete,
        name="comment_delete",
    ),
]
