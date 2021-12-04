
from django.urls import path
from . import views 
from .views import (
    ShopDetailView, 
    ShopListView,
    DetailView ,
    ShopCreateView,
    ShopUpdateView,
    ShopDeleteView
    
)
    
urlpatterns = [
    # path('',views.home , name= 'shop-home'),
    path('',ShopListView.as_view() , name= 'shop-home'),
    # url containing variable with route
    path('<int:pk>/', ShopDetailView.as_view(), name= 'shop-detail'),
    path('<int:pk>/update/', ShopUpdateView.as_view(), name= 'shop-update'),
    path('<int:pk>/delete/', ShopDeleteView.as_view(), name= 'shop-delete'),
    path('about/',views.about , name= 'shop-about'),
    path('new/',ShopCreateView.as_view() , name= 'shop-create'),
    
    
]

