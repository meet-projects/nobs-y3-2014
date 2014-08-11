from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'app/home.html')

def signup(request):
    return render(request, 'app/signup.html')

def search_results(request):
    return render(request, 'app/search_results.html')

def video(request):
    return render(request, 'app/video.html')

def profile(request):
    return render(request, 'app/profile.html')

def upload(request):
    return render(request, 'app/upload.html')
