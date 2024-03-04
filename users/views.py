from django.shortcuts import render
from django.views import generic
from .models import UserProfile

# Create your views here.

# @login_required
class UserDetail(generic.DetailView):
    """View user's profile information"""

    model = UserProfile
    template_name = "users/user_profile.html"
