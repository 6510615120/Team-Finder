from django.urls import path
from teamfinder_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about', views.about, name='about'),
]