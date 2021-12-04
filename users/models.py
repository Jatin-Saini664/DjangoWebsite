from django.db import models
from django.contrib.auth.models import User

from PIL import Image
# django provide it for us user model 
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # user for this profile on delete means what will django do if that user will get deleted 
    # cascade means if user it deleted then it will also delete profile 

    image = models.ImageField(default='default.jpg' , upload_to = 'profile_pic')
    # default.jpg is for those who dont have profile 
    # profile_pic is directory where this profile will be added 

    def __str__(self):
        # dunder method to display 
        return f'{self.user.username} Profile'

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        # we are using pillow to resize image and 
        img = Image.open(self.image.path)
        if(img.height>300 or img.width>300):
            output_size  = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

# Testing Expermintal Model 
class DemoConsumerProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # user for this profile on delete means what will django do if that user will get deleted 
    # cascade means if user it deleted then it will also delete profile 

    image = models.ImageField(default='default.jpg' , upload_to = 'profile_pic')
    # default.jpg is for those who dont have profile 
    # profile_pic is directory where this profile will be added 

    
    def __str__(self):
        # dunder method to display 
        return f'{self.user.username} Profile'

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        # we are using pillow to resize image and 
        img = Image.open(self.image.path)
        if(img.height>300 or img.width>300):
            output_size  = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)



