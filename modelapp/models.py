from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserModel(AbstractUser):
   
    phone_number = models.CharField(max_length=50, blank = True, null = True)
    code_number = models.CharField(max_length = 5, blank = True, null = True)



    
