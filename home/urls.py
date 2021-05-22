# from django.contrib import admin
# from django.urls import path, include
# from home import views


# from .views import ClassView, SubjectView



# urlpatterns = [
#     path('', views.index, name="home"),
#     path('signup', views.handleSignup, name="handleSignup"),
#     path('login', views.handleLogin, name="handleLogin"),
#     path('logout', views.handleLogout, name="handleLogout"),
#     path("contact", views.contact, name='contact'),


#     path("plans", views.plans, name='plans'),
#     path("cssNameOnImage", views.cssNameOnImage, name='cssNameOnImage'),

#     path("checkout", views.checkout, name='checkout'),
#     path("success", views.success, name='success'),
#     path("sheet", views.sheet, name='sheet'),
#     path("search", views.search, name='search'),


#    #  path("ClassViewContainer", views.ClassViewContainer, name='ClassViewContainer'),
#     path('class/', (ClassView.as_view()), name='ClassView'),
#     path('subject/', (SubjectView.as_view()), name='SubjectView'),
#     path('topic/', (TopicView.as_view()), name='TopicView'),
#     path('subtopic/', (SubTopicView.as_view()), name='SubTopicView'),
#     #path('explain/', (explain.as_view()), name='explain'),
#     path('download/', (download.as_view()), name='donwload'),
#     path('packages/', (packages.as_view()), name='packages'),
#     path('features/', (features.as_view()), name='features'),
#     path('payment/', (payments.as_view()), name='payment'),
#     path('images/', (images_row.as_view()), name='payment'),
#     path('image/<int:pk>/', views.image, name='image'),


# ]

from django.contrib import admin
from django.urls import path, include
from home import views

###--------------------------------------###

from django.contrib.auth.decorators import login_required
from .views import ClassView, SubjectView, TopicView, SubTopicView, download, packages, features, payments, images_row


# ###----------------Forgot Password-----------###
# from django.contrib.auth import views as auth_views
# ###--------------------------------------###

from django_email_verification import urls as email_urls





urlpatterns = [
    path('email/', include(email_urls)),
    path('', views.index, name="home"),
    path('signup', views.signup, name="signup"),
    path('quiz', views.quiz, name="quiz"),
    #path('login', views.login, name="login"),
    #path('signup', views.handleSignup, name="handleSignup"),
    path('login', views.LoginView.as_view(template_name='login.html'), name="handleLogin"),

    path('logout', views.handleLogout, name="handleLogout"),
    path("contact", views.contact, name='contact'),
    path("plans", views.plans, name='plans'),
    path("checkout/<int:plan_id>", views.checkout, name='checkout'),
    path("success/", views.success, name='success'),
    path("sheet", views.sheet, name='sheet'),
    path("search", views.search, name='search'),
    path("cssNameOnImage", views.cssNameOnImage, name='cssNameOnImage'),
    path("email_sent",views.email_sent, name='email_sent'),


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
    path('images/', (images_row.as_view()), name='images'),
    path('image/<int:pk>/', views.image, name='image'),

    ###----------------------Forgot Password------------------------###

    # path("password_reset/", auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name="password_reset"),
    # path("password_reset_/done/", auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    # path("password_reset_confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name="password_reset_confirm"),
    # path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),

   ###----------------------------------------------###


]
