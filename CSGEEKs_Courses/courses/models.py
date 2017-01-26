from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Member(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    pwd = models.CharField(max_length=200)
    logged_in = models.BooleanField(default=False)

    def __str__ (self):
    	return self.last_name

class Course(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=400, default="")
    img = models.CharField(max_length=200, default="")
    members = models.ManyToManyField(Member)

    def __str__ (self):
    	return self.title
