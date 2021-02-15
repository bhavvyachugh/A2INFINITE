from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('', views.index, name="home"),
    path('signup', views.handleSignup, name="handleSignup"),
    path('login', views.handleLogin, name="handleLogin"),
    path('logout', views.handleLogout, name="handleLogout"),
    path("contact", views.contact, name='contact'), 
    path("class_worksheet", views.class_worksheet, name='class_worksheet'), 
    path("subject_class_3_worksheet", views.subject_class_3_worksheet, name='subject_class-3_worksheet'), 


   
    
]
