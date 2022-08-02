
from django.urls import path
from . views import *
from .import views




app_name = 'project'


urlpatterns =[

    #path('',ProjectView.as_view(), name='home'),
    path('',views.home, name='home'),
     path('contact/' ,views.contactMe,name='contact'),
    
]


