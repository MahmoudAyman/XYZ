from __future__ import unicode_literals
import PIL
from django.db import models
from django.forms import ModelForm
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible
from django.conf import settings

# Create your models here.


@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.sub_path, filename)


class Member(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    pwd = models.CharField(max_length=200)
    logged_in = models.BooleanField(default=False)
    img = models.ImageField(upload_to=UploadToPathAndRename(os.path.join(settings.MEDIA_ROOT, 'upload')))    
    # upload_date=models.DateTimeField(auto_now_add =True)

    def __str__ (self):
        return self.last_name


    

class Course(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=400, default="")
    img = models.CharField(max_length=200, default="")
    members = models.ManyToManyField(Member)

    def __str__ (self):
    	return self.title

class Post(models.Model):
    title=models.CharField(max_length=200, default="")
    by = models.CharField(max_length=200, default="")
    date=models.DateField(auto_now_add=True)
    content=models.TextField()
    img = models.CharField(max_length=200, default="")
    course=models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Notification(models.Model):
    content=models.TextField()
    date=models.DateField(auto_now_add=True)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id)


class Video(models.Model):
    title=models.CharField(max_length=200, default="")
    url=models.CharField(max_length=400, default="")
    content=models.TextField()
    date=models.DateField(auto_now_add=True)
    by = models.CharField(max_length=200, default="")
    course=models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Assignment(models.Model):
    title=models.CharField(max_length=200, default="")
    content=models.TextField()
    date=models.DateField(auto_now_add=True)
    by = models.CharField(max_length=200, default="")
    course=models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Comment(models.Model):
    title=models.CharField(max_length=200, default="")
    content=models.TextField()
    date=models.DateField(auto_now_add=True)
    video=models.ForeignKey(Video, on_delete=models.CASCADE, default="")

    def __str__(self):
        return str(self.id)

class File(models.Model):
    data=models.FileField(upload_to="files/")
    date=models.DateField(auto_now_add=True)
    assign=models.ForeignKey(Assignment, on_delete=models.CASCADE)
    member=models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


        
