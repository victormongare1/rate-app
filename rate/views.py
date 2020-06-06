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
def search_results(request):
    if 'title' in request.GET and request.GET["title"]:
        search_term = request.GET.get("title")
        searched_projects =Project.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"users": searched_users})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})     
