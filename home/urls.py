
from django.contrib import admin
from django.urls import path, include
from home import views

###--------------------------------------###

from django.contrib.auth.decorators import login_required
from .views import ClassView, SubjectView, TopicView, SubTopicView, download, packages, features, payments, images_row


urlpatterns = [
    path('', views.index, name="home"),
    path('signup', views.handleSignup, name="handleSignup"),
    path('login', views.handleLogin, name="handleLogin"),
    path('logout', views.handleLogout, name="handleLogout"),
    path("contact", views.contact, name='contact'), 
    path("plans", views.plans, name='plans'), 
    path("checkout/<int:plan_id>", views.checkout, name='checkout'), 
    path("success/", views.success, name='success'),
    path("sheet", views.sheet, name='sheet'),
    path("search", views.search, name='search'), 
    path("cssNameOnImage", views.cssNameOnImage, name='cssNameOnImage'), 


    ###----------------------------------------------###

    path('class/', (ClassView.as_view()), name='ClassView'),
    path('subject/', (SubjectView.as_view()), name='SubjectView'),
    path('topic/', (TopicView.as_view()), name='TopicView'),
    path('subtopic/', (SubTopicView.as_view()), name='SubTopicView'),
   #  path('explain/', (explain.as_view()), name='explain'),
    path('download/', (download.as_view()), name='donwload'),
    path('packages/', (packages.as_view()), name='packages'),
    path('features/', (features.as_view()), name='features'),
    path('payment/', (payments.as_view()), name='payment'),
    path('images/', (images_row.as_view()), name='payment'),
    path('image/<int:pk>/', views.image, name='image'),

    ###----------------------Forgot Password------------------------###

    # path("password_reset/", auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name="password_reset"),
    # path("password_reset_/done/", auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    # path("password_reset_confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name="password_reset_confirm"),
    # path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),

# --------------------------------- base urls -------------------------------- #
    path('base/header', views.header, name="header"),
    path('base/navbar', views.navbar, name="navbar"),
    path('base/signin', views.signin, name="signin"),
    path('base/signout', views.signout, name="signout"),
    path('base/signup', views.signup, name="signup"),
    path('base/loader', views.loader, name="loader"),
]
