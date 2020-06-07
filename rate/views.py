from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile,Project,Review
from django.contrib.auth.models import User
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from .forms import ProfileForm,ProjectForm,ReviewForm
from django.http import HttpResponseRedirect

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    '''
    view route for home page
    '''
    posts=Project.objects.all()
    return render(request,'index.html',{"posts":posts})

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'title' in request.GET and request.GET["title"]:
        search_term = request.GET.get("title")
        searched_projects =Project.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"projects": searched_projects})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})     

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)        

@login_required(login_url='/accounts/login/')  
def create_profile(request):
    current_user = request.user
    if request.method=="POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile =form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect(home)
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')  
def profile(request,id): 
    try: 
        current_user = request.user
        profile = Profile.objects.filter(user_id=id).all()
        projects = Project.objects.filter(profile_id=current_user.profile.id).all()
        return render(request, 'profile.html', {"profile":profile, "projects":projects}) 
    except User.profile.RelatedObjectDoesNotExist:
        return redirect(create_profile)

@login_required(login_url='/accounts/login/')  
def new_post(request):
    current_user = request.user
    if request.method=='POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = current_user.profile
            project.save()
            return redirect(home)
    else:
        form = ProjectForm()
    return render(request, 'newpost.html',{"form":form})  


@login_required(login_url='/accounts/login/')  
def single_post(request, proj_id):
    project = Project.objects.get(pk=proj_id)
    reviews = Review.objects.filter(project_id=proj_id).all()
    current_user = request.user
    project = Project.get_project_by_id(proj_id)
    if request.method=='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user_id = current_user
            review.project_id = project
            review.overall_score = (review.design+review.usability+review.content)//3
            review.save()
            
    else:
        form=ReviewForm()
    return render(request,'singlepost.html',{"reviews":reviews,"form":form,"project":project})
