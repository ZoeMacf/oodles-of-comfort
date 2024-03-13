from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import RecipeCommentsForm
from .models import Recipe

class TestRecipeViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.recipe = Recipe(title="Recipe title", slug="recipe-title", author=self.user.userprofile,
                         prep_time='10 min', cook_time='30 min', recipe_steps='prepare the ingredients',
                         recipe_blurb='this is a recipe',
                         status=1)
        self.recipe.save()

    def test_render_recipe_detail_page_with_comment_form(self):
        response = self.client.get(reverse(
            'recipe_detail', args=['recipe-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Recipe title", response.content)
        self.assertIn(b"10 min", response.content)
        self.assertIn(b"30 min", response.content)
        self.assertIn(b"prepare the ingredients", response.content)
        self.assertIsInstance(
            response.context['recipe_comments_form'], RecipeCommentsForm)

    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        self.client.login(username="myUsername", password="myPassword")
        post_data = {'body': 'This is a test comment on a recipe.'}
        response = self.client.post(reverse('recipe_detail', args=['recipe-title']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Comment submitted successfully and is now awaiting approval!',
        response.content
        )
