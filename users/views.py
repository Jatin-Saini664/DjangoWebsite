from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import users
from .forms import UserRegistrationForm,  UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    # classes wil be converted to the html
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created ! You are now able to login')
            return redirect('user-login')
    else:
        form = UserRegistrationForm()

    context = {
        'form':form
    }
    return render(request,'users/register.html',context)

# decorator is added here so that we can prevent from going profile directly by urls
@login_required
def profile(request):
    
    # it will give us template to update forms but not provide current user information in form already 

    # if we pass model object related to it it will display relevent data 
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f' your accoun has been updated ')
            return redirect('user-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)        
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context=context)

