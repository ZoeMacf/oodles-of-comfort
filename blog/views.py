from django.shortcuts import render
from django.views import generic
from .models import Recipe
import random

# Create your views here.

# class RecipeCarousel(generic.ListView):
#     """View a randomised selection of recipes """
#     model = Recipe
#     template_name = "blog/index.html"


def RandomRecipes(request):
    """Assign the recipes to an object called all_recipes, randomise and display 4 to the view"""

    all_recipes = Recipe.objects.all()

    randomised_recipes = all_recipes.order_by("?")[:4]

    return render(
        request, "blog/index.html", {"randomised_recipes": randomised_recipes}
    )


class RecipeList(generic.ListView):
    """View all of the recipes"""

    model = Recipe
    template_name = "blog/recipe_list.html"


class RecipeDetail(generic.DetailView):
    """View a single recipe"""

    model = Recipe
    template_name = "blog/recipe_detail.html"
