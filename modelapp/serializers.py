from .models import UserModel
from rest_framework import serializers
from django.contrib.auth.models import User


class UserModelSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length = 50)
    password = serializers.CharField(max_length = 35, write_only=True)
    phone_number = serializers.CharField(max_length = 50)

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password','phone_number']
        
    

class LoginSerizalizer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25)
    password = serializers.CharField(max_length = 35)
    

    class Meta:
        model = UserModel 
        fields = ['username', 'password']
        


class VerifySerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25)
    code_number = serializers.CharField(max_length=5)

    class Meta:
        model = UserModel
        fields = ['username','code_number']