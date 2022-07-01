from django.contrib import admin
from django.urls import path
from school import views
urlpatterns = [
    path('',views.console),
    path('register',views.register),
    path('record',views.showrecords),
    path('email',views.send_mail),
    path('dashboard',views.console)
]
