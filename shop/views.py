from django.shortcuts import render
from django.http import HttpResponse
from .models import ShopDetails
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
# we can not use login decorator in class so we use mixin

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

class ShopListView (ListView):
    model = ShopDetails

    # this will look for an template of following pattern
    # <app>/<model>_<viewtype.html>.html
    # but we can change it using template_name 
    template_name = "shop/home.html"

    # now we were looping on context variable of name posts but here it is called
    # objectlist instead of post
    # we change this 
    context_object_name = "shop_details"
    
    # To see latest once at the top
    ordering = ['date_posted']
    #  ordering = ['-date_posted'] for doing opposite


class ShopDetailView (DetailView):
    model = ShopDetails

class ShopCreateView (LoginRequiredMixin, CreateView):
    model = ShopDetails
    # date will be created automatically
    
    # fileds we want to see in form
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

        

    # this will share view with update view template

class ShopUpdateView (LoginRequiredMixin,UserPassesTestMixin , UpdateView):
    model = ShopDetails
    # date will be created automatically
    
    # fileds we want to see in form
    fields = ['title','content']
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        shop = self.get_object()
        if shop.owner == self.request.user:
            return True
        return False


class ShopDeleteView (LoginRequiredMixin,UserPassesTestMixin ,DeleteView):
    model = ShopDetails
    success_url = '/shop'
    def test_func(self):
        shop = self.get_object()
        if shop.owner == self.request.user:
            return True
        return False