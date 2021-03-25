from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.models import User
from home.models import Contact
from datetime import datetime
import razorpay
from django.views.decorators.csrf import csrf_exempt

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


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent !')
    return render(request, 'contact.html')
 
def class_worksheet(request):
    return render(request,"class_worksheet.html")
    
 
def subject_class_2_worksheet(request):
    return render(request,"subject_class_2_worksheet.html")    
    
def subject_class_1_worksheet(request):
    return render(request,"subject_class_1_worksheet.html")    
    
def subject_class_ukg_worksheet(request):
    return render(request,"subject_class_ukg_worksheet.html")    
    
def subject_class_lkg_worksheet(request):
    return render(request,"subject_class_lkg_worksheet.html")    
    
def subject_class_nursery_worksheet(request):
    return render(request,"subject_class_nursery_worksheet.html")    

    
def topic_class_lkg_english_worksheet(request):
    return render(request, "topic_class_lkg_english_worksheet.html")

def a_sound_lkg_english_worksheet(request):
    return render(request,"a_sound_lkg_english_worksheet.html")        
    
    

def plans(request):
    return render(request,"plans.html")    

    return render(request, "subject_class_nursery_worksheet.html")
    

def payment(request):
    if request.method == 'POST':
        amount = 50000
        order_currency = 'INR'
        client = razorpay.Client(
            auth=('rzp_test_Ac2g1pJT7D9c69', 'd87OjvZuXZMT6FppcevvzxXU'))

        payment = client.order.create({'amount':amount, 'currency':currency,'payment_capture': '1'})   
    
   
    return render(request, "payment.html")
    
@csrf_exempt    
def success(request):
    return render(request, "success.html")    
