from django.shortcuts import render
from django.views import generic
from .models import Recipe

# Create your views here.

class RecipeList(generic.ListView):
    """View all of the recipes"""
    model = Recipe
    template_name = "blog/index.html"

class RecipeDetail(generic.DetailView):
    """View a single recipe"""
    model = Recipe
    template_name = "blog/recipe_detail.html"
    