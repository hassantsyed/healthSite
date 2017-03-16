"""train URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^browse/$', views.browse_trainers, name='browse_trainers'),
    url(r'^browse/trainers$', views.browse_trainers, name='browse_trainers'),
    url(r'^browse/nutritionists$', views.browse_nutritionists, name='browse_nutritionists'),
    url(r'^browse/doctors$', views.browse_doctors, name='browse_doctors'),
    url(r'^browse/(?P<username>[^/.]+)$', views.person, name='person'),
    url(r'^$', views.profile, name='profile'),
    url(r'^weight/$', views.weight, name='weight'),
    url(r'^addWeight/$', views.addWeight),
    url(r'^deleteWeight/$', views.deleteWeight)
]
