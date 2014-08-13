from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.models import User

def home(request):
	context = {'logged':False}
        return render(request, 'app/home.html')

def signup(request):
        context={'months':["January", "February", "March", "April", "May",
	"June", "July", "August", "September", "October", "November", "December"]}
        context["days"] = range(1, 32)
	context["years"] = range(1914, 2007)
        context['form'] = UserRegistrationForm()
	context['logged'] = False
        return render(request, 'app/signup.html', context)

class UserRegistrationForm(forms.Form):
        first_name = forms.CharField(label=u'first_name')
        last_name = forms.CharField(label=u'last_name')
        email = forms.CharField(label=u'Email')
        userName = forms.CharField(label=u'userName')
        password = forms.CharField(label=u'password',widget=forms.PasswordInput)
        day = forms.IntegerField(label=u'day')
        month = forms.IntegerField(label=u'month')
        year = forms.IntegerField(label=u'year')
        gender = forms.CharField(label=u'gender')

	 ##password_again = forms.CharField(label=u'password_again',widget=forms.PasswordInput)


def register(request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
	#TODO Add functionality to save
                email = form.cleaned_data['email']
                userName = form.cleaned_data['userName']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                password = form.cleaned_data['password']
                day = form.cleaned_data['day']
                month = form.cleaned_data['month']
                year = form.cleaned_data['year']
                gender = form.cleaned_data['gender']
                ##password_again = form.cleaned_data['password_again']
                ##if password != password_again:
                ##	return render(request, 'books/signup.html', {'form': UserRegistrationForm(), 'message': 'passwords did not match' })
                if len(User.objects.filter(username = userName)):
			return render(request, 'app/signup.html', {'form': UserRegistrationForm(), 'message': 'ERROR: email already exists' })
		elif "" in [email,  password, day, year, gender, month] or first_name == "" or last_name == "":
			return render(request, 'app/signup.html', {'form': UserRegistrationForm(), 'message': 'all fields should be filled' })
		else:
			user = User.objects.create_user(username = email, email=email, password=password, last_name=last_name, first_name=first_name)
			user.save()
			a = Profile(user = user, name = user.first_name + " " + user.last_name, email = user.email, userName = user.username)
			a.save()
			user = authenticate(email=email, password =password)
			login(request, user)
			context = {'user': request.user}
	
			return render(request, 'app/home.html', context)

def search_results(request):
    return render(request, 'app/search_results.html')

def video(request):
    return render(request, 'app/video.html')

def profile(request):
    return render(request, 'app/profile.html')

def upload(request):
    return render(request, 'app/upload.html')



def submitlogout(request):
	logout(request)
	return HttpResponseRedirect("home")


def submitlogin(request):

	Email = request.POST['email']
	Password = request.POST['password']
	user = authenticate(email=Email, password=Password)
	login(request, user)
	context = {'user': request.user}
	return my_render(request, 'books/homepage.html', context)
