from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
    path('list/', persons_list, name="persons_list"),
    path('new/', persons_new, name="persons_new"),
]
