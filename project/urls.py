
from django.urls import path
from . views import *
from .import views
#from .views import MyView





app_name = 'project'


urlpatterns =[

    #path('',ProjectView.as_view(), name='home'),
    path('',views.home, name='home'),
     path('contact/' ,views.contactMe,name='contact'),

     path('pdf-download/' ,views.resumeDownload,name='pdf-download'),  
     #path('new-download/',, name='new-download')

     path('myview/',  GeneratePdf.as_view(), name='myview'),
    
]


