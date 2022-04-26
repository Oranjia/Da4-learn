from cgitb import html
import re

from django.http import HttpResponse
from regex import F
from urllib3 import HTTPResponse, Retry
from django.template import loader
from django.shortcuts import render

def page_2003_view(requst):
    html="<h1>这是第一个页面</h1>"
    return HttpResponse(html)

def pagen_view(requst,pg):
    html="这是编号为%s的网页"%(pg)
    return HttpResponse(html)

def cal_view(requst,n,op,m):
    if op not in ["add","sub","mul"]:
        return HttpResponse("滚犊子")
    
    result= 0
    if op == "add":
        result=n+m
    elif op == "sub":
        result=n-m
    elif op =="mul":
        result=n*m
    
    return HttpResponse("结果为：%s"%(result))

def test_html(request):
    #方案一
    # t=loader.get_template("test_html.html")
    # html=t.render()
    # return HttpResponse(html)
    dic={
        "username":"cyc",
        "age":22,
        "daima":"<script> alert(111) </script>"
    }

    dic_new={}
    dic_new["int"]=88
    dic_new["list"]=["Tom","Sam"]
    dic_new["dic"]={"a":9,"b":10}
    dic_new["func"]=say_hi
    dic_new["class_obj"]=Dog()
    return render(request,"test_html.html",{"dics":dic,"dic_news":dic_new})  # 返回多个字典

def say_hi():
    return "hi"

class Dog:
    def say(self):
        return "wangwang"




def test_if_for(request):
    dic={}
    dic["x"]=11
    dic["lst"]=["Tom","Same","hahah"]
    return render(request,"test_if_for.html",dic)

def test_mycal(request):
    if request.method=="GET":
        return render(request,"mycal.html")
    if request.method=="POST":
        x=int(request.POST["x"])
        y=int(request.POST["y"])
        op=request.POST["op"]

        result=0
        if op=="add":
            result=x+y
        elif op=="sub":
            result=x-y
        return render(request,"mycal.html",locals())  #lacals可以自己组件字典

def base_view(request):
    return render(request,"base.html")

def music_view(request):
    return render(request,"music_index.html")

def sport_view(request):
    return render(request,"sport_index.html")