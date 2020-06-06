from rest_framework import serializers
from .models import Profile,Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','user', 'profile_pic', 'bio','contacts')