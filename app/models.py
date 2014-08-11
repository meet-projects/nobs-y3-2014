from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    	path = models.CharField(max_length=50)
    	title = models.CharField(max_length=50)
    	description = models.CharField(max_length=100)
	uploader = models.ForeignKey(User)
	date = models.DateField()
	
class Profile(models.Model):
	#def get_code:
        user = models.OneToOneField(User)
	email = models.CharField(max_length = 200)
        name = models.CharField(max_length = 40)
        userName = models.CharField(max_length = 40)
        day = models.IntegerField()
	month = models.IntegerField()
        year = models.IntegerField(label=u'year')
	gender = forms.CharField(label=u'gender')
##        photo = models.ImageField(upload_to = "books/static/images")
