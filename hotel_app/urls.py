from django.conf.urls import include, url
from django.contrib import admin
from hotel_app.views import *

urlpatterns = [
    url(r'^$', index),
]
