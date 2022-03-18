from django.db import models
from acount.models import Profile
from django.db.models.fields.related import ForeignKey
from django.db.models.fields.related import ManyToManyField
from blog.models import Tag

# Create your models here.
class Project(models.Model):
    profile=ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True)
    tags=ManyToManyField(Tag)
    title=models.CharField(max_length=200)
    slug=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True,upload_to='project/')
    source_link=models.CharField(null=True,blank=True, max_length=200)
    demo_link=models.CharField(null=True,blank=True, max_length=200)
    vote=models.IntegerField(null=True,blank=True,default=1)
    state=models.BooleanField(default=False,choices=((False,'Activate'),(True,'Deactivate')))
    created_at=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now=True)
    
def __str__(self):
        return self.title
