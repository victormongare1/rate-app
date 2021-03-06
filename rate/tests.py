from django.test import TestCase
from .models import Project,Profile

# Create your tests here.
class ProfileTestClass(TestCase):
    '''
    test class to test methods of the profile class
    '''
    def setUp(self):
        self.profile=Profile(user="victor",profile_pic="pic",bio="person",contacts='vicmongz254@gmail.com')

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.profile.delete_profile()
        profiles= Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

class ProjectTestClass(TestCase):
    '''
    test class to test methods of the  Project class
    '''
    def setUp(self):
        self.profile=Profile(user="victor",profile_pic="pic",bio="person",contacts="vicmongz254@gmail.com")
        self.project=Project(image="image",title="image",description="nice",link='https;//image',profile=self.profile)

    def test_save_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0) 

    def test_search_method(self):
        self.assertQuerysetEqual(Project.objects.filter(title__icontains='image'), ["<Project: image>"])  

    def test_delete_method(self):
        self.project.delete_project()
        projects=Project.objects.all()
        self.assertTrue(len(projects) === 0) 

           

