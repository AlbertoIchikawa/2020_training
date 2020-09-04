"""assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from news import loginViews, homeNewsViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', loginViews.LoginViewSet.as_view()),
    path('home/', homeNewsViews.HomeNewsSet.as_view()),
    path('abroad/', homeNewsViews.AbroadNewsSet.as_view()),
    path('japan/', homeNewsViews.JapanNewsSet.as_view()),
    path('local/', homeNewsViews.LocalNewsSet.as_view()),
    path('business/', homeNewsViews.BusinessNewsSet.as_view()),
    path('science/', homeNewsViews.ScienceNewsSet.as_view()),
    path('gossip/', homeNewsViews.GossipNewsSet.as_view()),
    path('sports/', homeNewsViews.SportsNewsSet.as_view())
]
