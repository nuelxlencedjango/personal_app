
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

    