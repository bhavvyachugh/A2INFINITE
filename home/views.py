from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.models import User
from home.models import Contact
#from home.models import Sheet
from datetime import datetime
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

###-----------------------------------------------------###


from django.views import View
from .models import ClassDetails, Subject, Topic, SubTopic, Explain
from django.core.paginator import Paginator
import os
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import requests
from io import StringIO
from django.views.generic import View
from django.http import HttpResponse


###-------------------------------------------------------###

# from blog.models import Post

# Create your views here.



def index(request):
    return render(request,"html/index.html")

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
    return render(request, 'html/contact.html')
 
def sheet(request):

   sheet = Sheet.objects.all()
   return render(request,'html/sheet.html', {'sheet' : sheet})



def worksheet_class(request):
    return render(request,"html/worksheet_class.html")
    
 
def subject_class_2_worksheet(request):
    return render(request,"html/subject_class_2_worksheet.html")    
    
def subject_class_1_worksheet(request):
    return render(request,"html/subject_class_1_worksheet.html")    
    
def subject_class_ukg_worksheet(request):
    return render(request,"html/subject_class_ukg_worksheet.html")    
    
def subject_class_lkg_worksheet(request):
    return render(request,"html/subject_class_lkg_worksheet.html")    
    
def subject_class_nursery_worksheet(request):
    return render(request,"html/subject_class_nursery_worksheet.html")    

    
def topic_class_lkg_english_worksheet(request):
    return render(request, "html/topic_class_lkg_english_worksheet.html")

def topic_class_nursery_english_worksheet(request):
    return render(request, "html/topic_class_nursery_english_worksheet.html")

def topic_class_nursery_maths_worksheet(request):
    return render(request, "html/topic_class_nursery_maths_worksheet")

def a_sound_lkg_english_worksheet(request):
    return render(request,"html/a_sound_lkg_english_worksheet.html")        
    
    

def plans(request):
    return render(request,"html/plans.html")    

    return render(request, "html/subject_class_nursery_worksheet.html")
    

def checkout(request):
    if request.method == 'POST':
        amount = 50000
        order_currency = 'INR'
        client = razorpay.Client(
            auth=('rzp_test_Ac2g1pJT7D9c69', 'd87OjvZuXZMT6FppcevvzxXU'))

        checkout = client.order.create({'amount':amount, 'currency':currency,'payment_capture': '1'})   
    
   
    return render(request, "html/checkout.html")
    
@csrf_exempt    
def success(request):
    return render(request, "html/success.html")   


def search(request):
    if request.method == 'POST':
        searchh = request.POST['search']

        if searchh:
            match = Sheet.objects.filter(Q(name__icontains=searchh) |
                                        Q(image__icontains=searchh))


            if match:
                return render(request, 'html/search.html', {'search': match})
            else:
                messages.error(request, 'no result found')
        else:
            return HttpResponseRedirect('/search')
    return render(request,'html/search.html')           



    ###-------------------------------------------------------------------------------------------------------------###


class ClassView(View):
    def get(self, request):
        classdata = ClassDetails.objects.all()
        return render(request, "frontend/ClassViewContainer.html",{
            "classdata" : classdata
        })  


class SubjectView(View):
    def get(self, request):
        classId = request.GET.get("class", None)
        try:
            data = ClassDetails.objects.get(id=classId)
        except ClassDetails.DoesNotExist:
            return redirect("ClassView")
        if classId == None:
            return redirect("ClassView")
        Subjectsdata = Subject.objects.filter(className = data)
        return render(request, "frontend/SubjectViewContainer.html",{
            "classdata" : Subjectsdata
        })


class TopicView(View):
    def get(self, request):
        subjectId = request.GET.get("subject", None)
        try:
            data = Subject.objects.get(id=subjectId)
        except Subject.DoesNotExist:
            return redirect("ClassView")
        if subjectId == None:
            return redirect("ClassView")
        Topicdata = Topic.objects.filter(Subject = data)
        return render(request, "frontend/TopicViewContainer.html",{
            "classdata" : Topicdata
        })


class SubTopicView(View):
    def get(self, request):
        topicId = request.GET.get("topic", None)
        try:
            data = Topic.objects.get(id=topicId)
        except Topic.DoesNotExist:
            return redirect("ClassView")
        if topicId == None:
            return redirect("ClassView")
        SubtopicData = SubTopic.objects.filter(topic = data)
        return render(request, "frontend/SubTopicViewContainer.html",{
            "classdata" : SubtopicData
        })


class explain(View):
    def get(self, request):
        subtopicId = request.GET.get("subtopic", None)
        try:
            data = SubTopic.objects.get(id=subtopicId)
        except SubTopic.DoesNotExist:
            return redirect("ClassView")
        if subtopicId == None:
            return redirect("ClassView")
        explaindata = Explain.objects.filter(SubTopic = data)
        page = request.GET.get('page', 1)
        paginator = Paginator(explaindata, 1)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        return render(request, "frontend/explainContainer.html",{
            "classdata" : users,
            "topicid" : subtopicId
        })

        
class download(View):
    def get(self, request):
        try:
            downloadid = request.GET.get("id", None)
            typedata = request.GET.get("type", None)
            if downloadid == None or typedata == None:
                return redirect("ClassView")
            search_item = Explain.objects.get(id=downloadid)
            if typedata == "black":
                blackphoto =  Image.open(search_item.imgBlack)
                filename = search_item.imgBlack.url.split("/")[-1]
                filetype = search_item.imgBlack.url.split(".")[-1]
            elif typedata == 'white':
                blackphoto =  Image.open(search_item.imgWhite)
                filename = search_item.imgWhite.url.split("/")[-1]
                filetype = search_item.imgWhite.url.split(".")[-1]
            else:
                blackphoto =  Image.open(search_item.imgColor)
                filename = search_item.imgColor.url.split("/")[-1]
                filetype = search_item.imgColor.url.split(".")[-1]
            response = HttpResponse(content_type="image/jpeg")
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            blackphoto.save(response, "png")
            return response
        except:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))