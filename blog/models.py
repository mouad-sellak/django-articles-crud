from django.db import models
from django.db.models.fields import  CharField,TextField, DateTimeField,IntegerField
from django.db.models.fields.related import  ForeignKey,ManyToManyField
from django.utils.text import slugify

# Create your models here.
class Article(models.Model):
    title=CharField(max_length=200,unique=True)
    description = TextField(null=True)
    created = DateTimeField(auto_now_add=True)
    picture= models.ImageField(null=True, upload_to="articles/")
    slug=models.SlugField(max_length=200, unique=True,  db_index=True, null=True, blank=True)
    updated = DateTimeField(auto_now=True)
    category= ForeignKey('Category',null=True, on_delete=models.SET_NULL)
    author=ForeignKey('Author',null=True,on_delete=models.SET_NULL)
    tags=ManyToManyField('Tag')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs): #*args : allow list of args,  **kwargs diction of args
        if not self.slug:
            self.slug=slugify(self.title)
        super().save(*args, **kwargs)


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
    
class Author(models.Model):
    name=CharField(max_length=20)
    picture=models.ImageField(null=True,upload_to='authors/')
    created = DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    