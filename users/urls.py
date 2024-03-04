# from . import views
from .views import UserDetail
from django.urls import path

urlpatterns = [
path('<int:pk>/', UserDetail.as_view(), name='user_profile'),
]