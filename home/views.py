from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.models import User
from home.models import Contact
import json
#from home.models import Sheet
from datetime import datetime,timedelta
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .serializer import TopicSerializer
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
###-----------------------------------------------------###


from django.views import View
from .models import ClassDetails, Subject, Topic, SubTopic, Explain, Feature, Package, Orders, Subscriptions
from django.core.paginator import Paginator
import os
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import requests
from io import StringIO
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from .forms import UserSignUpForm 
from bootstrap4.templatetags.bootstrap4 import bootstrap_form
import hmac
from django.utils import timezone
import logging

logger = logging.getLogger()

from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy

from werkzeug.wrappers.json import _JSONModule

#from a2infinity.settings import dumps

###-------------------------------------------------------###

# from blog.models import Post

# Create your views here.



def index(request):
    return render(request,"index.html")

def signup(request):
    return render(request,"signup.html")

# def handleSignup(request):
#     if request.method == 'POST':
#         form = UserSignUpForm(request.POST)
#         if form.is_valid():
#             #print(json.dumps(form.cleaned_data,indent=4,default=str))
#             obj2 = form.save()
#             formnew = UserSignUpForm()
#             messages.success(request, "Successfully Loged-in")
#             return render(request, 'form_modeldata/add_modeldata_successfull.html',dict(form=formnew))
#         else:
#             return render(request, 'form_modeldata/add_modeldata.html',dict(form=form))


def handleLogin(request):    

    user = None
    if request.method == "POST":
        loginusername = request.POST['loginusername'] 
        loginpassword = request. POST['loginpassword']
        

        user = authenticate(username=loginusername, password=loginpassword)
        
    if user is not None:
        login(request, user)
        messages.success(request, "Successfully Loged-in")

        if 'next' in request.POST:
            return redirect(request.POST.get('next'))
        
        else:
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

def cssNameOnImage(request):
   return render(request,'cssNameOnImage.html')
      

def plans(request):
    packages = Package.objects.all()
    try:
        current_subscription = Subscriptions.objects.filter(user=request.user).last()
        subscription_end_data = current_subscription.created_at + timedelta(days = 365)
        sub_package = current_subscription.package

        if timezone.now() < subscription_end_data:
            subscribed = True
            end_date = subscription_end_data

        else:
            subscribed = False
            end_date = None

    except:
        #logger.exception("Fatal error")
        subscribed = False
        sub_package = None
        end_date = None
        subscription_end_data = None

    new_array = []
    for package in packages:
        if package == sub_package:
            package.subscription = subscribed
            package.end_date = subscription_end_data
        else:
            package.subscription = False
            package.end_date = None
        new_array.append(package)

    print(new_array)
    return render(request,"plans.html",dict(plans = new_array))
    

@login_required(login_url=reverse_lazy('home'))
def checkout(request,plan_id):
    plan = Package.objects.get(id=plan_id)
    
    order_amount = plan.pkg_price*100
    order_currency = 'INR'
    order_receipt = f'{request.user} :: {plan.id} - {plan.pkg_name}'
    client = razorpay.Client(auth=('rzp_test_Ac2g1pJT7D9c69', 'd87OjvZuXZMT6FppcevvzxXU'))
    response = client.order.create({'amount':order_amount, 'currency':order_currency,'receipt':order_receipt,'payment_capture': '1'})

    Orders(
            order_id = response['id'],
            package = plan,
            full_response = json.dumps(response,indent=4,default=str),
            razorpay_payment_id = "",
            razorpay_order_id = "",
            razorpay_signature = "",
            user = request.user,
            status = "Pending",
            amount = order_amount,
        ).save()

    context = dict(
            amount = order_amount/100,
            order_id = response['id'],
        )

    return render(request, "checkout.html",context)

@login_required(login_url=reverse_lazy(''))
@csrf_exempt    
def success(request):
    try:
        response = request.POST

        params_dict = {
            'razorpay_payment_id' : response['razorpay_payment_id'],
            'razorpay_order_id' : response['razorpay_order_id'],
            'razorpay_signature' : response['razorpay_signature']
        }

        order = Orders.objects.get(order_id = params_dict['razorpay_order_id'])

        client = razorpay.Client(auth=('rzp_test_Ac2g1pJT7D9c69', 'd87OjvZuXZMT6FppcevvzxXU'))

        client.utility.verify_payment_signature(params_dict)

        order.razorpay_payment_id = params_dict['razorpay_payment_id']
        order.razorpay_order_id = params_dict['razorpay_order_id']
        order.razorpay_signature = params_dict['razorpay_signature']
        order.status = "Paid"
        order.save()

        Subscriptions(
            package = order.package,
            user = order.user,
            amount = order.amount,
            ).save()

        return render(request, "success.html")
    except Exception as e:
        logger.exception("Fatal error")
        return render(request, "unsuccess.html")




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

def check_user_subscription_status(request):
    user_logged_in = False

    # check user is logged in
    if request.user.is_authenticated:
        user_logged_in = True

    package = None
    end_date = None
    subscribed = False
    end_date = None
    subscribed_classes = []
    if user_logged_in:
        # check user is subscribed
        try:
            current_subscription = Subscriptions.objects.filter(user=request.user).last()
            subscription_end_data = current_subscription.created_at + timedelta(days = 365)
            subscription_package = current_subscription.package
            package = subscription_package

            if timezone.now() < subscription_end_data:
                subscribed = True
                end_date = subscription_end_data
                subscribed_classes = list(package.classes.all().values_list('id',flat=True))
            else:
                subscribed = False
                end_date = None
        except:
            logger.exception("Failed No subscription")
            subscribed = False
            end_date = None

    return request.user, user_logged_in, subscribed, package, end_date, subscribed_classes



class ClassView(View):
    def get(self, request):
        user, user_logged_in, subscribed, package, end_date, subscribed_classes = check_user_subscription_status(request)
        classdata = ClassDetails.objects.all()
        for i in range(0,len(classdata)):
            if subscribed and classdata[i].id in subscribed_classes:
                classdata[i].susbscribed = True
            else:
                classdata[i].susbscribed = False

        data = serializers.serialize("json", classdata)
        return render(request, "ClassViewContainer.html",{
            "classdata" : classdata
        })  







class SubjectView(View):
    def get(self, request):
        user, user_logged_in, subscribed, package, end_date, subscribed_classes = check_user_subscription_status(request)

        classId = int(request.GET.get("class", None))
        try:
            data = ClassDetails.objects.get(id=classId)
        except ClassDetails.DoesNotExist:
            logger.exception()
            return redirect("ClassView")
        if classId == None:
            logger.debug(f"class Id is None")
            return redirect("ClassView")



        condition1 = not classId in subscribed_classes
        condition2 = not data.freeForAll
        condition1_2 = condition1 or condition2
        data_dict = data.__dict__

        #logger.debug(dumps(locals()))

        if condition1 and condition2:
            logger.debug(f"not classId in subscribed_classes or not data.freeForAll")
            return redirect("ClassView")

        Subjectsdata = Subject.objects.filter(className = data)

        if classId in subscribed_classes:
            sub_subscribed = True
        else:
            sub_subscribed = False

        return render(request, "SubjectViewContainer.html",{
            "classdata" : Subjectsdata,"sub_subscribed": sub_subscribed
        })

class TopicView(View):
    def get(self, request):
        user, user_logged_in, subscribed, package, end_date, subscribed_classes = check_user_subscription_status(request)

        subjectId = request.GET.get("subject", None)
        
        try:
            subobj = Subject.objects.get(id=subjectId)
        except subobj.DoesNotExist:
           return redirect("ClassView")
        
        if subjectId == None:
            return redirect("ClassView")
      
        # CHeck w.r.t class

        classobj = subobj.className
        classobj_dict = classobj.__dict__

        if classobj.id in subscribed_classes:
            topicsobj = Topic.objects.filter(Subject = subobj)
            return render(request, "TopicViewContainer.html",{
                "data" : topicsobj, 'topic_subscribed':True, 'subobj': subobj, 'classobj': classobj
            })
        else:
            if classobj.freeForAll:
                if subobj.freeForAll:
                    topicsobj = Topic.objects.filter(Subject = subobj)
                    return render(request, "TopicViewContainer.html",{
                        "data" : topicsobj, 'topic_subscribed':False, 'subobj': subobj, 'classobj':classobj
                    })
                else:
                    return redirect("ClassView")
            else:
                return redirect("ClassView")



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


# class explain(View):
#     def get(self, request):
#         subtopicId = request.GET.get("subtopic", None)
#         try:
#             data = SubTopic.objects.get(id=subtopicId)
#         except SubTopic.DoesNotExist:
#             return redirect("ClassView")
#         if subtopicId == None:
#             return redirect("ClassView")
#         explaindata = Explain.objects.filter(SubTopic = data)
#         print(explaindata)
#         page = request.GET.get('page', 1)
#         paginator = Paginator(explaindata, 1)
#         try:
#             users = paginator.page(page)
#         except PageNotAnInteger:
#             users = paginator.page(1)
#         except EmptyPage:
#             users = paginator.page(paginator.num_pages)
#         return render(request, "explainContainer.html",{
#             "classdata" : users,
#             "topicid" : subtopicId
#         })


def image(request, pk):
    user, user_logged_in, subscribed, package, end_date, subscribed_classes = check_user_subscription_status(request)

    try:
        explainObj = Explain.objects.get(pk=pk)
    except explainObj.DoesNotExist:
        return redirect("ClassView")
    if pk == None:
        return redirect("ClassView")

    subtopicObj = explainObj.SubTopic
    subtopicObj_dict = subtopicObj.__dict__

    topicObj = subtopicObj.topic
    topicObj_dict = topicObj.__dict__

    subObj = topicObj.Subject
    subObj_dict = subObj.__dict__

    classObj = subObj.className
    classObj_dict = classObj.__dict__

    all_schools = False
    if classObj.id in subscribed_classes:
        if package.id == 5:
            all_schools = True
        return render(request, "image.html", {'class':explainObj,'subscribed':True,'all_schools': all_schools})
    else:
        if classObj.freeForAll:
            if subObj.freeForAll:
                if topicObj.freeForAll:
                    if subtopicObj.freeForAll:
                        if explainObj.freeForAll:
                            return render(request, "image.html", {'class':explainObj,'subscribed':False})
                        else:
                            return redirect("ClassView")
                    else:
                        return redirect("ClassView")
                else:
                    return redirect("ClassView")
            else:
                return redirect("ClassView")

        else:
            return redirect("ClassView")




    


class images_row(View):
    def get(self, request):
        user, user_logged_in, subscribed, package, end_date, subscribed_classes = check_user_subscription_status(request)

        subtopicId = request.GET.get("subtopic", None)
        try:
            subtopicObj = SubTopic.objects.get(id=subtopicId)
        except subtopicObj.DoesNotExist:
            return redirect("ClassView")
        if subtopicId == None:
            return redirect("ClassView")



        topicObj = subtopicObj.topic
        topicObj_dict = topicObj.__dict__

        subObj = topicObj.Subject
        subObj_dict = subObj.__dict__


        classObj = subObj.className
        classObj_dict = classObj.__dict__

        if classObj.id in subscribed_classes:
            explaindata = Explain.objects.filter(SubTopic = subtopicObj)
            totalcount = Explain.objects.filter(SubTopic = subtopicObj).count()

            return render(request, "images_row.html", {'explaindata':explaindata,'totalcount':totalcount,'countfree': len(explaindata),'subscribed':True})
        else:
            if classObj.freeForAll:
                if subObj.freeForAll:
                    if topicObj.freeForAll:
                        if subtopicObj.freeForAll:
                            explaindata = Explain.objects.filter(SubTopic = subtopicObj).filter(freeForAll=True)
                            totalcount = Explain.objects.filter(SubTopic = subtopicObj).count()
                            return render(request, "images_row.html", {'explaindata':explaindata,'totalcount':totalcount,'countfree': len(explaindata),'subscribed':False})
                        else:
                            return redirect("ClassView")
                    else:
                        return redirect("ClassView")
                else:
                    return redirect("ClassView")

            else:
                return redirect("ClassView")



        
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


    ###----------------------------------Forgot password views---------------------------------------------------------------------------###
           