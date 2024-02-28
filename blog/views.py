from django.shortcuts import render
from django.views import generic
from .models import Recipe

# Create your views here.

class RecipeCarousel(generic.ListView):
    """View a selection of recipes at random"""
    model = Recipe
    template_name = "blog/index.html"


class RecipeList(generic.ListView):
    """View all of the recipes"""
    model = Recipe
    template_name = "blog/recipe_list.html"

class RecipeDetail(generic.DetailView):
    """View a single recipe"""
    model = Recipe
    template_name = "blog/recipe_detail.html"
    