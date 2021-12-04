from django.contrib import admin
from .models import Profile,DemoConsumerProfile

# Register your models here so that we can see it in the admin page gui with super user we created with with our username and password 
admin.site.register(Profile)
admin.site.register(DemoConsumerProfile)

