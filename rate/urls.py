from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    url(r'^search/',views.search_results, name='search_results'),
    url(r'^profile/(\d+)',views.profile,name = 'profile'),
    url(r'^createprofile',views.create_profile,name="create_profile"),
    url(r'^accounts/profile',views.profile,name='profile'),
    url(r'^api/profiles/$',views.ProfileList.as_view()),
    url(r'^api/projects/$',views.ProjectList.as_view()),
    url(r'^project/(\d+)',views.single_post,name='project'),
    url(r'^new/post$',views.new_post,name="new_post"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)