from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="rotary/members/")
    fb_link = models.CharField(max_length=200)
    ld_link = models.CharField(max_length=200)
    tw_link = models.CharField(max_length=200)
    
    def __str__(self):
         return self.name
    



class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)
    def __str__(self):
         return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title',unique=True)
    date = models.DateField()
    categories = models.ManyToManyField('Category')
    content = models.TextField()
    image = models.ImageField(blank=True,upload_to='rotary/posts')
    
    
    def __str__(self):
         return self.title
     
class PostImage(models.Model):
    image = models.ImageField(upload_to='rotary/posts/')
    post = models.ForeignKey('Post',on_delete=models.CASCADE)   
    def __str__(self):
         return self.post.title
        
    
class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title',unique=True)
    location = models.CharField(max_length=200)
    date = models.DateField()
    categories = models.ManyToManyField('Category')
    content = models.TextField()
    map = models.CharField(max_length=1000,null=True)
    cost = models.IntegerField()
    youtube_link = models.CharField(max_length=1000)
    image = models.ImageField(blank=True,upload_to='rotary/projects')
    
    
    def __str__(self):
         return self.title
       

class ProjectImage(models.Model):
    image = models.ImageField(upload_to='rotary/projects/')
    project = models.ForeignKey('Project',on_delete=models.CASCADE)   
    def __str__(self):
         return self.project.title