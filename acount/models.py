from django.db import models
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Profile(models.Model):
    user=OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=80)
    username=models.CharField(max_length=80,unique=True,null=True,blank=True)
    email=models.EmailField(max_length=120,unique=True,null=True,blank=True)
    head_line=models.CharField(max_length=120,unique=True,null=True,blank=True)
    bio=models.TextField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True,upload_to='profiles/',default='profiles/default,png')
    resume_link=models.CharField(max_length=120,null=True,blank=True)
    github_link=models.CharField(max_length=120,null=True,blank=True)
    linkedin_link=models.CharField(max_length=120,null=True,blank=True)
    youtube_link=models.CharField(max_length=120,null=True,blank=True)
    website_link=models.CharField(max_length=120,null=True,blank=True)
    state=models.BooleanField(default=False,choices=((False,'Activate'),(True,'Deactivate')))
    created_at=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now=True)
    id=models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4)
    
def __str__(self):
        return self.name
    
    
