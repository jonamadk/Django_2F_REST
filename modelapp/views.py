from django.shortcuts import render
from django.db.models.query import QuerySet
from rest_framework.views import APIView
from django.http import request
from .serializers import UserModelSerializer, LoginSerizalizer, VerifySerializer
from .models import UserModel
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .utils import send_sms
from .otpcode import otp_generator
from rest_framework import generics
import random


class UserRegisteration(APIView):
   

    def post(self, request, *args, **kwargs):
       
        serializer = UserModelSerializer(data = request.data)
        print(serializer)
        if serializer.is_valid():
            data = serializer.validated_data
            print(data)
            user = UserModel.objects.create(email = data.get('email'),
                                            username = data.get('username'),
                                            phone_number = data.get('phone_number'),
                                            password = make_password(data.get('password')))

            user.save()
            return Response(status=status.HTTP_201_CREATED)


class UserListView(generics.ListAPIView):

    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

            
class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = LoginSerizalizer(data = request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            user = authenticate(username=data.get('username'),
                                 password=data.get('password'))
    
            if user is not None:
                phone_number = user.phone_number
                user = UserModel.objects.get(username=data.get('username'))
                user.code_number = otp_generator()
                user.save()
                code = user.code_number
                send_sms(code, phone_number,)
            
                return Response({"status":"User Created"},
                                status =status.HTTP_200_OK)
            else:
                return Response({"status":"no user with such credentials"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                

class VerifyView(APIView):

    def post(self, request, *args, **kwargs):
        seralizer = VerifySerializer(data = request.data)
        if seralizer.is_valid():
            data = seralizer.validated_data
            user = UserModel.objects.get(username = data.get("username"))
            code = user.code_number
            if code == data.get("code_number"):
                return Response({"status":"OTP Verified"},
                                 status=status.HTTP_200_OK)
            else:
                return Response({"status":"Incorrect OTP"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



            
     





