from django.contrib import admin
from django.urls import path
from . import views  #把music下面的views.py引进来

urlpatterns = [
    path("all_book",views.all_book),
    path("update_book/<int:book_id>",views.update_book),
    path("delete_book",views.delete_book),
    path("set_session",views.set_session),
    path("get_session",views.get_session)
]

