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
        self.image=Image(image="image",name="image",caption="nice",profile=self.profile)
    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0) 

    def test_delete_method(self):L
        self.image.delete_image()
        images=Image.objects.all()
        self.assertTrue(len(images) > 0)        

