from django.contrib import admin
# from .models import Catagory
# from .models import Product (or)
from .models import *

# Register your models here.
admin.site.register(Catagory)
admin.site.register(Product)

'''We can use to display some lists

   class adminCatagory(admin.ModelAdmin):
        list_display = ('name', 'image', 'description')
        
    admin.site.register(Catagory, adminCatagory)'''