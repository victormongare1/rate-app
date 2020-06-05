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
    contacts=models.CharField(max_length = 100)

class Project(models.Model):
    '''
    project class to define project objects
    '''
    image=models.ImageField(upload_to = 'images/')
    title=models.CharField(max_length = 100)
    description=models.CharField(max_length = 100)
    link=models.CharField(max_length = 100)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)

    @classmethod
    def search_by_title(cls,search_term):
    project = cls.objects.filter(title__icontains=search_term)
    return project 

class Review(models.Model):
    '''
    review class to define review objects
    '''
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    project_id=models.ForeignKey(Project, on_delete=models.CASCADE,null=True)
    comment=models.TextField(blank=True)
    design=models.IntegerField()
    usability=models.IntegerField()
    content=models.IntegerField()