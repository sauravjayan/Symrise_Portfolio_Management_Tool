from django.db import models
from django.contrib.auth.models import User, PermissionsMixin

# Create your models here.
class Account(User, PermissionsMixin):

    def __str__(self):
        return self.username 
        
    
