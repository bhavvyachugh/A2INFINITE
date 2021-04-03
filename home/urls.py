from django.contrib import admin
from django.urls import path, include
from home import views

###--------------------------------------###


from .views import ClassView, SubjectView, TopicView, SubTopicView, explain, download


###--------------------------------------###


urlpatterns = [
    path('', views.index, name="home"),
    path('signup', views.handleSignup, name="handleSignup"),
    path('login', views.handleLogin, name="handleLogin"),
    path('logout', views.handleLogout, name="handleLogout"),
    path("contact", views.contact, name='contact'), 
    #path("worksheet_class", views.worksheet_class, name='worksheet_class'), 
    path("subject_class_2_worksheet", views.subject_class_2_worksheet, name='subject_class_2_worksheet'), 
    path("subject_class_1_worksheet", views.subject_class_1_worksheet, name='subject_class_1_worksheet'), 
    path("subject_class_ukg_worksheet", views.subject_class_ukg_worksheet, name='subject_class_ukg_worksheet'), 
    path("subject_class_lkg_worksheet", views.subject_class_lkg_worksheet, name='subject_class_lkg_worksheet'), 

    path("subject_class_nursery_worksheet", views.subject_class_nursery_worksheet, name='subject_class_nursery_worksheet'), 

    path("topic_class_lkg_english_worksheet", views.topic_class_lkg_english_worksheet, name='topic_class_lkg_worksheet'), 
    path("topic_class_nursery_english_worksheet", views.topic_class_nursery_english_worksheet, name='topic_class_nursery_english_worksheet'), 
    path("topic_class_nursery_maths_worksheet", views.topic_class_nursery_maths_worksheet, name='topic_class_nursery_maths_worksheet'), 
    path("a_sound_lkg_english_worksheet", views.a_sound_lkg_english_worksheet, name='a_sound_lkg_english_worksheet'), 

    path("plans", views.plans, name='plans'), 

    path("subject_class_nursery_worksheet", views.subject_class_nursery_worksheet, name='subject_class_nursery_worksheet'),
    path("checkout", views.checkout, name='checkout'), 
    path("success", views.success, name='success'), 
    path("sheet", views.sheet, name='sheet'),
    path("search", views.search, name='search'), 


    ###----------------------------------------------###

    path('class/',ClassView.as_view(), name='ClassView'),
    path('subject/', SubjectView.as_view(), name='SubjectView'),
    path('topic/', TopicView.as_view(), name='TopicView'),
    path('subtopic/', SubTopicView.as_view(), name='SubTopicView'),
    path('explain/', explain.as_view(), name='explain'),
    path('download/', download.as_view(), name='donwload')


    ###----------------------------------------------###
 
]
