from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.


# we need to customize our user
class User(AbstractUser):
    
    # we have to add the custom email field with unique true
    # becuse the by defaul email field is optional and can be overwirte
    
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['email']
    pass