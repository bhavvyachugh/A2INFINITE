from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.models import User
from home.models import Contact
import json
#from home.models import Sheet
from datetime import datetime
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .serializer import TopicSerializer


from django.views import View
from .models import ClassDetails, Subject, Topic, SubTopic, Explain, Package, Feature
from django.core.paginator import Paginator
import os
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import requests
from io import StringIO
from django.views.generic import View
from django.http import HttpResponse, JsonResponse

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
 
def sheet(request):

   sheet = Sheet.objects.all()
   return render(request,'sheet.html', {'sheet' : sheet})


def topic_class_lkg_english_worksheet(request):
    return render(request, "topic_class_lkg_english_worksheet.html")

def topic_class_prenursery_english_worksheet(request):
    return render(request, "topic_class_prenursery_english_worksheet.html")

def topic_class_prenursery_maths_worksheet(request):
    return render(request, "topic_class_prenursery_maths_worksheet.html")

def topic_class_nursery_english_worksheet(request):
    return render(request, "topic_class_nursery_english_worksheet.html")

def topic_class_nursery_maths_worksheet(request):
    return render(request, "topic_class_nursery_maths_worksheet.html")

def topic_class_lkg_maths_worksheet(request):
    return render(request, "topic_class_lkg_maths_worksheet.html")

def topic_class_lkg_hindi_worksheet(request):
    return render(request, "topic_class_lkg_hindi_worksheet.html")   

def plans(request):
    return render(request,"plans.html")    

def cssNameOnImage(request):
    return render(request,"cssNameOnImage.html")    

    

def checkout(request):
    if request.method == 'POST':
        amount = 50000
        order_currency = 'INR'
        client = razorpay.Client(
            auth=('rzp_test_Ac2g1pJT7D9c69', 'd87OjvZuXZMT6FppcevvzxXU'))

        checkout = client.order.create({'amount':amount, 'currency':currency,'payment_capture': '1'})   
    
   
    return render(request, "checkout.html")
    
@csrf_exempt    
def success(request):
    return render(request, "success.html")   


def search(request):
    if request.method == 'POST':
        searchh = request.POST['search']

        if searchh:
            match = Sheet.objects.filter(Q(name__icontains=searchh) |
                                        Q(image__icontains=searchh))


            if match:
                return render(request, 'search.html', {'search': match})
            else:
                messages.error(request, 'no result found')
        else:
            return HttpResponseRedirect('/search')
    return render(request,'search.html')           

###-------------------------------------------------------------------------------------------------------------###


class ClassView(View):
    def get(self, request):
        classdata = ClassDetails.objects.all()
        return render(request, "ClassViewContainer.html",{
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
        return render(request, "SubjectViewContainer.html",{
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
        data1  = TopicSerializer(Topicdata, many=True)
        return render(request, "TopicViewContainer.html",{
            "data" : data1.data
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
        return render(request, "SubTopicViewContainer.html",{
            "classdata" : SubtopicData
        })        

    def image(request, pk):
      img_id = Explain.objects.get(pk=pk)
      print(img_id)
      return render(request, "image.html", {'class':img_id})


class images_row(View):
    def get(self, request):
        subtopicId = request.GET.get("subtopic", None)
        try:
            data = SubTopic.objects.get(id=subtopicId)
        except SubTopic.DoesNotExist:
            return redirect("ClassView")
        if subtopicId == None:
            return redirect("ClassView")
        explaindata = Explain.objects.filter(SubTopic = data)
        return render(request, "images_row.html", {'explaindata':explaindata})

        
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


class packages(View):
    def get(self, request):
        all_plans = Package.objects.all()
        return render(request, "packages.html", {'all_plans':all_plans})


class features(View):
    def get(self, request):
        feature_id = request.GET.get("feature", None)

        try:
            data = Package.objects.get(id=feature_id)
        except Package.DoesNotExist:
            return redirect("packages")

        if feature_id == None:
            return redirect("packages")

        features_data = Feature.objects.filter(pkg_name=data)

        print(features_data)

        return render(request, "features.html", {'features_data':features_data})



class payments(View):
    def get(self, request):
        try:
            pkg_id = int(request.GET.get("pkg"))
            package = Package.objects.get(id=pkg_id)
        except (ValueError, TypeError, Package.DoesNotExist):
            return redirect("packages")
        client = razorpay.Client(
            auth=('rzp_test_Ac2g1pJT7D9c69', 'd87OjvZuXZMT6FppcevvzxXU')
        )
        payment = client.order.create(
            {
            'amount': package.pkg_price * 100,
            'currency': 'INR',
            'payment_capture': '1'
            }
        )
        return render(request, "payment.html", {'payment': payment})
                
