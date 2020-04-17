from django.contrib import admin

# Register your models here.

from apps.models import *
admin.site.register([Catagory,Tag,Blog])
