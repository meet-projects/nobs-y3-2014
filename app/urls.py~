from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='sign up'),
    url(r'^search_results/', views.search_results, name='search results'),
    url(r'^video/', views.video, name='video'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^submitlogin$', views.submitlogin),
    url(r'^submitregister$', views.register),        
    
    url(r'^submitlogout$', views.submitlogout),
)
