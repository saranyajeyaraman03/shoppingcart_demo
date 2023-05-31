from django.contrib import admin
from django.urls import path,include
from .models import *

# Register your models here.

urlpatterns =[
    path('admin/',admin.site.urls),
    path('',include('shops.urls')),
]
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','image','description')

admin.site.register(Catagory,CategoryAdmin)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite)

