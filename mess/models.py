from django.db import models

# Create your models here.
class food(models.Model):
    user_no=models.AutoField
    username=models.CharField(max_length=20,primary_key=True,unique=True)
    email=models.EmailField(max_length=20,unique=True)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=16)
    