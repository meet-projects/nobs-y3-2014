from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'app/home.html')

def signup(request):
    return HttpResponse("- This is the sign up page -")

def search_results(request):
    return HttpResponse("- This is the search results -")

def video(request):
    return HttpResponse("- This is the play video page -")

def profile(request):
    return HttpResponse("- This is the profile page -")

def upload(request):
    return HttpResponse("- This is the upload page -")