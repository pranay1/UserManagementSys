from django.contrib import admin
from django.urls import path , include
from deviceDetail import views

urlpatterns = [
   path('',views.index,name="index"),
   path('create_device/',views.create_device,name="create_device"),
   path('display_device_info/<int:id>',views.display_device_info,name="display_device_info"),
   path('display_device_info/delete_device_info/<int:id>',views.delete_device_info,name="delete_device_info"),
]
