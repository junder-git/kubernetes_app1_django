"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views  #importing our view file

#urlprefix='paintapp/'
urlpatterns = [
    path('', views.viewHome, name='viewHome'), #mapping the homepage function//  urlprefix+'', views.viewHome, name='home'
    path('accounts/', include('allauth.urls')),  # new
    path('admin/', admin.site.urls, name='admin'),
    path('viewRooms/', views.viewRooms, name='viewRooms'), #mapping the homepage function /// path(urlprefix+'viewRooms/', views.viewRooms, name='viewRooms'),
    path('addRooms/', views.addRooms, name='addRoom'), #mapping the homepage function /// path(urlprefix+'addRooms/', views.addRooms, name='addRoom'),
    path('viewRooms/<slug:slug>/', views.viewRoom, name='slugRoom')
]