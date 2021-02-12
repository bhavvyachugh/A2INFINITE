from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.models import User
# from blog.models import Post

# Create your views here.



def index(request):
    return render(request,"index.html")


def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        school = request.POST['school']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.school = school
        myuser.save()
        messages.success(request, "Your account has been created successfully")
        return redirect('home')

        #Password confirmation
    if pass1 != pass2:
        messages.error(request, "Passwords Do not Match")
        return redirect('home')

    else:
        return HttpResponse("404 page not founds")
        

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        

        user = authenticate(username=loginusername, password=loginpassword)
        
    if user is not None:
        login(request, user)
        messages.success(request, "Successfully Loged-in")
        return redirect('home')
        

    else:
     messages.error(request, "try again")
     return redirect('home')


        

       
       
    return HttpResponse('login')


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged-out")
    return redirect('home')
    return HttpResponse('logout')                