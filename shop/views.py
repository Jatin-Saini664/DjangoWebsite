from django.shortcuts import render
from django.http import HttpResponse
from .models import ShopDetails
# Create your views here.
detail=[
    {
        'owner':'Balaji',
        'title':'shop 1',
        'content':'this is first shop',
        'date_posted':'October 1 2021'
    },
    {
        'owner':'Aggarwalji',
        'title':'shop 2',
        'content':'this is second shop',
        'date_posted':'October 2 2021'
    }

]
def home(request):
    context = {
        'shop_details':ShopDetails.objects.all(),
        'title':"Home Page"
        # shop_details is accesible from the html file so we loop on the list
    }
    return render(request,'shop/home.html',context) # sub directory inside templates folder , returns http response or exception 

def about(request):
    return render(request,'shop/about.html')

def default(request):
    return render(request, 'shop/default.html')




