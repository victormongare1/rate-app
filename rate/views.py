from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile,Project,Review
from django.contrib.auth.models import User
from django.http  import HttpResponse,Http404,HttpResponseRedirect
# Create your views here.
@login_required(login_url='/accounts/login/')
def home():
    '''
    view route for home page
    '''
    projects=Project.objects.all()
    return render(request,{'projects':projects})

@login_required(login_url='/accounts/login/')
    
