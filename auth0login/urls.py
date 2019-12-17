from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.index),
    path('check/', views.check_user_info, name="index"),
    path('get/', views.get_user_info, name='get user info'),
    path('get/edit_user_info', views.edit_user_info, name='edit user info'),
    path('get/update_user_info', views.update_user_info, name='update user info'),
    path('get/delete_user_info', views.delete_user_info, name='update user info'),
    path('logout', views.logout),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
]