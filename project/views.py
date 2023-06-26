from django.core.mail import send_mail
from django.conf import settings

from django.core.paginator import Paginator 

from django.views.generic import (ListView)
from django.db.models import Q
from django.shortcuts import render,HttpResponse
#from django.contrib import auth, messages
from .pdf import pdfFiles
from django.http import HttpResponse
import datetime


from datetime import datetime
from .models import *






# generating and printing the SECRET_KEY
#print('begin:',get_random_secret_key(),':end')



class ProjectView(ListView):
    model = ProjectDetails
    template_name = "project/home.html"

    def get_queryset(self, *args, **kwargs):
        qs = super(ProjectView, self).get_queryset(*args, **kwargs)
        qs =qs.order_by("-date_added")
        return qs


def home(request):
    product =ProjectDetails.objects.all()
   

    def getIp(request):

        address = request.META.get('HTTP_X_FORWARDED_FOR')
        print("ip address:",address)
        if address:
            ip =  address.split(',')[-1].strip()
            print('2nd ip:',ip)

        else:
            ip = request.META.get('REMOTE_ADDR') 
            print('3rd ip :')

        return ip

    ip = getIp(request) 
    u = User(user=ip)
    print('4th ip:', ip)
    result = User.objects.filter(Q(user__icontains=ip))
    if len(result) == 1:
        print('user exists')

    elif len(result) > 1:
        print('user exists')   

    else:
        u.save()    
        print('unique user')

    count = User.objects.all().count() 
    print("total number is :", count)   

    context={'product':product,'count':count}



    return render(request,'project/home.html',context)







def contactMe(request):
  

    if request.method =='POST':
        message_name = request.POST['message-name']
        message_phone = request.POST.get("message-phone" ,False)
        message_email = request.POST['message-email']
        message  = request.POST['message']
       # products_name =request.POST['property']
        products = request.POST.getlist('property')


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


        return render(request ,'project/email.html',{'message_name' :message_name}) 

    
    return render(request ,'project/contact.html') 



def resumeDownload(request):
    
    convertPdf = pdfFiles('project/pdf.html')
    return HttpResponse(convertPdf,content_type="application/pdf")


        



from django.http import HttpResponse
from django.views.generic import View

from .utils import render_to_pdf #created in step 4

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
             'today': datetime.date.today(), 
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('project/first.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
    





