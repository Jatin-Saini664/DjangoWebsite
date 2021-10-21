from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    # classes wil be converted to the html
    if request.metho == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
    else:
        form = UserCreationForm()

    context = {
        'form':form
    }
    return render(request,'users/register.html',context)


