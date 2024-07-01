from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    profile = ProfileSerializer(required=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        