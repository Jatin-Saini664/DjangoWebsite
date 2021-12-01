
from django.urls import path
from . import views 
from .views import PostDetailView, PostListView,DetailView
urlpatterns = [
    # path('',views.home , name= 'shop-home'),
    path('',PostListView.as_view() , name= 'shop-home'),
    
    # url containing variable with route
    path('<int:pk>/', PostDetailView.as_view(), name= 'shop-detail'),
    path('about/',views.about , name= 'shop-about'),
]

