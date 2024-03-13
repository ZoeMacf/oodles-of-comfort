from django.test import TestCase
from .forms import RecipeCommentsForm


class TestRecipeCommentsForm(TestCase):

    def test_form_is_valid(self):
        recipe_comments_form = RecipeCommentsForm({'body': 'This is a tasty recipe!'})
        self.assertTrue(recipe_comments_form.is_valid() , msg='Form is not valid')

    def test_form_is_not_valid(self):
        recipe_comments_form = RecipeCommentsForm({'body': ''})
        self.assertFalse(recipe_comments_form.is_valid() , msg='Form is valid')