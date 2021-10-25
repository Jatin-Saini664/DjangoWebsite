from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# we are using signals so that when a new user is created and it is saved it will give signal here so that user is created now its our turn to create a function that will tie a profile and with out user

@receiver(post_save,sender=User)
def create_profile(sender , instance , created , **kwargs):
    if(created):
        Profile.objects.create(user=instance)
        
@receiver(post_save,sender=User)
def save_profile(sender , instance  , **kwargs):
    instance.profile.save()