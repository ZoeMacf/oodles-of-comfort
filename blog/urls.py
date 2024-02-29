from . import views
from django.urls import path

urlpatterns = [
    path("", views.RandomRecipes, name="home"),
    path("<slug:pk>/", views.RecipeDetail.as_view(), name="recipe_detail"),
    path("recipes", views.RecipeList.as_view(), name="recipe_list"),
]
