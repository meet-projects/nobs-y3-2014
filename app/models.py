from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    	path = models.CharField(max_length=50)
    	title = models.CharField(max_length=50)
    	description = models.CharField(max_length=100)
	author = models.ForeignKey(User)
	date = models.DateField()
