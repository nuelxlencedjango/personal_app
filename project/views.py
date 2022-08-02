
from multiprocessing import context
from pyexpat.errors import messages
from unittest import result
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django_filters.views import FilterView
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from .models import *
from django.shortcuts import render ,redirect ,get_object_or_404
from django.views.generic import (
    ListView ,DetailView, CreateView, UpdateView ,DeleteView,TemplateView )







from django.shortcuts import render,redirect ,get_object_or_404, resolve_url
from django.contrib import auth, messages
import json

import requests
from django.utils import timezone


from django.http import HttpResponse,JsonResponse, request
from django.forms import inlineformset_factory


from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin





class ProjectView(ListView):
    model = ProjectDetails
    template_name = "project/home.html"



    def get_queryset(self, *args, **kwargs):
        qs = super(ProjectView, self).get_queryset(*args, **kwargs)
        qs =qs.order_by("-date_added")
        return qs

def home(request):
    product =ProjectDetails.objects.all()
    context={'product':product}
    return render(request,'project/home.html',context)







def contactMe(request):
  

    if request.method =='POST':
        message_name = request.POST['message-name']
        message_phone = request.POST.get("message-phone" ,False)
        message_email = request.POST['message-email']
        message  = request.POST['message']
       # products_name =request.POST['property']
        products = request.POST.getlist('property')




        # seend a mail
        # the order in which  to  pass arugument in the parameters is important
        send_mail(
            message_name , # email subject
            #message_phone, #phone no
            message_email , # from email 
            message ,      # main message
            #products, # items

            [settings.EMAIL_HOST_USER], # recipient, to email
        fail_silently=False)
        
        
        #contacts = ContactUs(name=message_name ,phone=message_phone ,email=message_email ,message=message)
        contacts = ContactUs()
        contacts.name =message_name
        contacts.phone = message_phone
        contacts.email = message_email
        contacts.selected_properties = products
        contacts.message = message
        contacts.save()


        return render(request ,'email.html',{'message_name' :message_name}) 

    else:
        return render(request ,'contact.html') 