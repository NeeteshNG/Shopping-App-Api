# users/models.py

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.email
