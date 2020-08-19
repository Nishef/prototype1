from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,null=True,default='')
    description = RichTextField(blank=True,null=True)
    #tags = ArrayField(models.CharField(max_length=255,unique=False,blank=True),unique=False,blank=True,default=list)
    
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ["-created_at","-updated_at"]
    
    def __str__(self):
        return self.title
    
    
    
    