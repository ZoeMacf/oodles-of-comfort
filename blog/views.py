from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.db.models import Q
from .forms import RecipeCommentsForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Recipe, Comment
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

def recipe_search(request):

    if request.method == "POST":
        search = request.POST['search']
        recipes = Recipe.objects.filter(title__contains=search)

        return render(request, 
        "blog/recipe_search.html",
        {'search' :search,
        'recipes' :recipes})


def recipe_detail(request, slug):
    """ Will display one recipe from the model Recipe"""

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()
    recipe_comments_form = RecipeCommentsForm()

    if request.method == "POST":
        recipe_comments_form = RecipeCommentsForm(data=request.POST)
    if recipe_comments_form.is_valid():
        comment = recipe_comments_form.save(commit=False)
        comment.author = request.user.userprofile
        comment.recipe = recipe
        comment.save()
        messages.add_message(
        request, messages.SUCCESS,
        'Comment submitted successfully and is now awaiting approval!'
    )

    return render(
        request,
        "blog/recipe_detail.html",
        {"recipe": recipe,
        "comments" : comments,
        "comment_count": comment_count,
        "recipe_comments_form": recipe_comments_form,
        },
    )

def edit_comment(recipe, slug, comment_id):
    """ Edit posted comments"""
    if request.method == "POST":

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        recipe_comments_form = CommentForm(data=request.POST, instance=comment)

        if recipe_comments_form.is_valid() and comment.author == request.user:
            comment = recipe_comments_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))
