from django.db import models
from django.db.models.fields import  CharField,TextField, DateTimeField,IntegerField
from django.db.models.fields.related import  ForeignKey,ManyToManyField

# Create your models here.
class Article(models.Model):
    title=CharField(max_length=200,unique=True)
    description = TextField(null=True)
    created = DateTimeField(auto_now_add=True)
    picture= models.ImageField(null=True, upload_to="articles/")
    updated = DateTimeField(auto_now=True)
    category= ForeignKey('Category',null=True, on_delete=models.SET_NULL)
    tags=ManyToManyField('Tag')

    def __str__(self):
        return self.title


class Category(models.Model):
    
    name=CharField(max_length=20)
    state=IntegerField(default=0,choices=( (0,"disable"),(1,"enable")) )
    #state=IntegerField(default=0)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=CharField(max_length=20)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    