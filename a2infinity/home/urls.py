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
    path("subject_class_2_worksheet", views.subject_class_2_worksheet, name='subject_class_2_worksheet'), 
    path("subject_class_1_worksheet", views.subject_class_1_worksheet, name='subject_class_1_worksheet'), 
    path("subject_class_ukg_worksheet", views.subject_class_ukg_worksheet, name='subject_class_ukg_worksheet'), 
    path("subject_class_lkg_worksheet", views.subject_class_lkg_worksheet, name='subject_class_lkg_worksheet'), 
    path("subject_class_nursery_worksheet", views.subject_class_nursery_worksheet, name='subject_class_nursery_worksheet'), 
    path("topic_class_lkg_english_worksheet", views.topic_class_lkg_english_worksheet, name='topic_class_lkg_worksheet'), 
    path("a_sound_lkg_english_worksheet", views.a_sound_lkg_english_worksheet, name='a_sound_lkg_english_worksheet'), 

    
]
