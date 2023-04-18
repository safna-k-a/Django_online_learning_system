from django.contrib import admin
from Myapp.models import Category, Course_details,Languages,Cart,Offer,Payment

# Register your models here.
admin.site.register(Category)
admin.site.register(Languages)
admin.site.register(Course_details) 
admin.site.register(Cart) 
admin.site.register(Offer) 
admin.site.register(Payment) 
