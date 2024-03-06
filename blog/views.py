from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe
import random

# Create your views here.

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


def recipe_detail(request, slug):
    """ Will display one recipe from the model Recipe"""

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()

    return render(
        request,
        "blog/recipe_detail.html",
        {"recipe": recipe,
        "comments" : comments,
        "comment_count": comment_count,
        },
    )
