from django.contrib import admin
from django.urls import path, include
from home import views


from .views import ClassView, SubjectView



urlpatterns = [
    path('', views.index, name="home"),
    path('signup', views.handleSignup, name="handleSignup"),
    path('login', views.handleLogin, name="handleLogin"),
    path('logout', views.handleLogout, name="handleLogout"),
    path("contact", views.contact, name='contact'), 
    path("topic_class_lkg_english_worksheet", views.topic_class_lkg_english_worksheet, name='topic_class_lkg_worksheet'), 
    path("topic_class_prenursery_english_worksheet", views.topic_class_prenursery_english_worksheet, name='topic_class_prenursery_english_worksheet'), 
    path("topic_class_prenursery_maths_worksheet", views.topic_class_prenursery_maths_worksheet, name='topic_class_prenursery_maths_worksheet'), 
    path("topic_class_nursery_english_worksheet", views.topic_class_nursery_english_worksheet, name='topic_class_nursery_english_worksheet'), 
    path("topic_class_lkg_maths_worksheet", views.topic_class_lkg_maths_worksheet, name='topic_class_lkg_maths_worksheet'), 
    path("topic_class_lkg_hindi_worksheet", views.topic_class_lkg_hindi_worksheet, name='topic_class_lkg_hindi_worksheet'), 

    path("plans", views.plans, name='plans'), 

    path("checkout", views.checkout, name='checkout'), 
    path("success", views.success, name='success'), 
    path("sheet", views.sheet, name='sheet'),
    path("search", views.search, name='search'),
    

   # path("ClassViewContainer", views.ClassViewContainer, name='ClassViewContainer'), 
     path('class/',ClassView.as_view(), name='ClassView'),
     path('subject/', SubjectView.as_view(), name='SubjectView'),

 
]
