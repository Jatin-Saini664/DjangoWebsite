from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import users

# Create your views here.

def register(request):
    # classes wil be converted to the html
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('shop-home')
    else:
        form = UserCreationForm()

    context = {
        'form':form
    }
    return render(request,'users/register.html',context)


