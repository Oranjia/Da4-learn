from django.contrib import admin
from django.urls import path
from . import views  #把music下面的views.py引进来

urlpatterns = [
    path("index",views.index_view)
]
