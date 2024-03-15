from .models import Comment
from django import forms


class RecipeCommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)
