from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


admin.site.register(Location)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(CityCategory)
admin.site.register(Resturant)
admin.site.register(ResturantCategory)
admin.site.register(Menu)
admin.site.unregister(Group)



admin.site.site_header  =  "Foodie Admin"  
admin.site.site_title  =  "Foodie Admin site"
admin.site.index_title  =  "Foodie Admin"