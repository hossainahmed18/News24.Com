"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import urls
from django.urls import path
from blogapp import views
from blogapp.views import getcreate
from blogapp.views import index
from blogapp.views import getAuthor
from blogapp.views import getsingle
from blogapp.views import getTopic
from blogapp.views import getlogin
from blogapp.views import getlogout

from blogapp.views import getprofile
from blogapp.views import getupdate
from blogapp.views import getdelete
from blogapp.views import getregister
from blogapp.views import getcategory
from blogapp.views import addcategory
from blogapp.views import getcatupdate
from blogapp.views import getcatdelete
from blogapp.views import getmessage
from blogapp.views import getsearch
from blogapp.views import getchange



urlpatterns = [
    path('', index, name="index"),
    path('author/<name>', getAuthor, name="author"),
    path('single/<int:id>', getsingle, name="single"),
    path('topic/<name>', getTopic, name="topic"),
    path('login', getlogin, name="login"),
    path('logout', getlogout, name="logout"),
    path('create', getcreate, name="create"),
    path('profile', getprofile, name="profile"),
    path('update/<int:pid>', getupdate, name="update"),
    path('delete/<int:id>', getdelete, name="delete"),
    path('register', getregister, name="register"),
    path('category', getcategory, name="category"),
    path('add_category/category', addcategory, name="add_category"),
    path('update_category/category/<name>', getcatupdate, name="update_category"),
    path('delete_category/category/<name>', getcatdelete, name="delete_category"),
    path('message', getmessage, name="message"),
    path('search', getsearch, name="search"),
    path('change', getchange, name="change")



]
