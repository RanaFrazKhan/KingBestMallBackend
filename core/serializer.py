from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

#serizlier for exclusing is in url for frontend
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=UserProfile
        fields=['Fname', 'Lname','Mobile','Country','State','City','Zip','Address','role','Pic']

class ProfilePostSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=['Fname', 'Lname','Mobile','Country','State','City','Zip','Address','role','Pic','user','Activation_Key']

class Contact_Us_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Contact_Us
        fields=['Name','Email','Phone','Message']
