from django.db.models.signals import post_save
from django.contrib.auth.models import User 
from django.dispatch import receiver 
from .models import UserProfile

# creation and setting up of signals file - https://www.devhandbook.com/django/user-profile/
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, username=instance.username)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.userprofile.save()