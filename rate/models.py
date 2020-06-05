from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    '''
    profile class to define profile objects
    '''
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to = 'images/')
    bio=models.CharField(max_length = 100)
    contacts=models.CharField(max_length = 60)
