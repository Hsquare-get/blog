from django.db import models

# Create your models here.

class Users(models.Model):
    useremail = models.CharField(primary_key=True, max_length=20)
    username = models.CharField(max_length=40)
    userpassword = models.CharField(max_length=16)