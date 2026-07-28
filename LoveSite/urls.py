"""
URL configuration for LoveSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from www.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
path('test1', test1, name='test1'),
path('test2', test2, name='test2'),
path('test3', test3, name='test3'),
path('test4', test4, name='test4'),
path('test5', test5, name='test5'),

]
