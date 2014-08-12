from django.db import models
from django.contrib.auth.models import User	

class Profile(models.Model):
        user = models.OneToOneField(User)
	email = models.CharField(max_length = 200)
        name = models.CharField(max_length = 40)
        user_name = models.CharField(max_length = 40)
        birth_date = models.DateField()
	joined_date = models.DateField(auto_now_add=True)
        image_path = models.CharField(max_length = 40)

class Video(models.Model):
    	path = models.CharField(max_length=50)
    	title = models.CharField(max_length=50)
    	description = models.CharField(max_length=100)
	uploader = models.ForeignKey(Profile)
	date = models.DateField(auto_now_add=True)
	tags = models.CharField(max_length=100)
	location = models.CharField(max_length=26)

#video = Video(path="1.mp4", title="Riots in Ukraine", description="Crazy footage of the riots in Ukraine", tags="riot riots ukraine putin russiabecrazy", location="Crimea, Ukraine", uploader=None)

