

from django.db import models

from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.shortcuts import reverse

from cloudinary.models import CloudinaryField
#from matplotlib.backend_bases import LocationEvent
#from matplotlib.pyplot import title
# Create your models here.





class ProjectDetails(models.Model):
    projectName =models.CharField(max_length=200, blank=True, null=True)
    description =models.TextField(max_length=200, blank=True, null=True)
    functionality1 =models.CharField(max_length=200, blank=True, null=True)
    functionality2 =models.CharField(max_length=200, blank=True, null=True)
    functionality3 =models.CharField(max_length=200, blank=True, null=True)
    functionality4 =models.CharField(max_length=200, blank=True, null=True)
    functionality5 =models.CharField(max_length=200, blank=True, null=True)
    technology =models.CharField(max_length=200, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    img = CloudinaryField(blank=True,null=True)

    def __str__(self):
        return self.projectName

        

    class Meta:
        #db_table='accommodation' 

        verbose_name_plural='Property'

    def get_add_to_cart(self):

        return reverse('product:add-to-cart' ,kwargs={
            "pk":self.pk
        })    





class ContactUs(models.Model):

   name = models.CharField(max_length=100) 
   email = models.EmailField(unique = False) 
   phone = models.CharField(max_length=20) 
   selected_properties =models.CharField(max_length=100) 

   message = models.TextField(max_length=200)


   class Meta:
      verbose_name_plural = "ContactMe"

   def __str__(self):
      return self.name 




class User(models.Model):
    user =models.TextField(default=None)

    def __str__(self):
        return self.user