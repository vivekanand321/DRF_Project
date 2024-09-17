from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
    title=models.CharField(max_length=30,blank=False,null=False)
    description=models.CharField(max_length=500,blank=False,null=False)
    duration=models.IntegerField(blank=False,null=False)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    price=models.IntegerField(blank=False,null=False)
    discount=models.IntegerField(blank=False,null=False)
    thumbnail=models.CharField(max_length=200,blank=False,null=False)
