from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from users.models import Profile
# from .models import Profile
# new forms so that we can add desired field like email and can make form according to us not like default
class UserRegistrationForm(UserCreationForm):
    # it inherits from UserceationForm
    email = forms.EmailField()

    class Meta:
        # here we definew models we would interact with
        model = User
        fields= ['username','email','password1' , 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields= ['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']





