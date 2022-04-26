"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cgitb import html
from django import views
from django.contrib import admin
from django.urls import path
from . import views  # . 就是当前目录

urlpatterns = [
    path('admin/', admin.site.urls),

    #http://127.0.0.1:8000/page/2003/
    path("page/2003/",views.page_2003_view),  #视图函数就是接受请求，返回相应
    path("page/<int:pg>",views.pagen_view),  #path转换器，可以匹配任意数字结尾的网页，path按照顺序，优先级按照顺序

    #http://127.0.0.1:8000/整数/操作符/整数
    path("<int:n>/<str:op>/<int:m>",views.cal_view),
    path("test_html",views.test_html),
    path("test_if_for",views.test_if_for),
    path("mycal",views.test_mycal),
    path("base",views.base_view),
    path("music_index",views.music_view),
    path("sport_index",views.sport_view)


    

]
