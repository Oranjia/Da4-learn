from doctest import REPORT_UDIFF
import re
from urllib import response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from matplotlib.pyplot import title
from post import POST
from .models import User,Content
import hashlib


# Create your views here.
def reg_view(request):
    #注册
    #GET返回页面

    if request.method=="GET":
        return render(request,"user/register.html")
    # POST处理提交数据
       
    elif request.method=="POST":
        username=request.POST["username"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        #1、密码要保持一致 
        if password1 != password2:
            return HttpResponse("两次输入密码不一致")

        #哈希算法--给定明文，计算出一段定长得不可逆得值
        m=hashlib.md5()
        m.update(password1.encode())
        password_m=m.hexdigest()

        # 2、当前用户名是否可以用 
        old_users=User.objects.filter(username=username)
        if old_users:
            return HttpResponse("用户名字已经注册了")
        # 3、插入数据明文处理密码先

        try:  #防止并发写入问题
            user=User.objects.create(username=username,pass_word=password_m)
        except Exception as e:
            print("--create user error %s"%(e))
            return HttpResponse("用户已经注册了")

        #免登录一天
        request.session["username"]=username
        request.session["uid"]=user.id    #拿到刚刚注册好的用户的主键，这样查起来比较的快

        #TO 修改session 储存时间为1天，原来默认14天
        return HttpResponseRedirect("/index/index")

def login_view(request):
    if request.method=="GET":
        #获取登陆页面，检查登录状态，如果登录了，显示已经登录
        if request.session.get("username") and request.session.get("uid"):
            #return HttpResponse("已经登录了")
            return HttpResponseRedirect("/index/index")
        #检查cookie
        c_username=request.COOKIES.get("username")
        c_uid=request.COOKIES.get("uid")
        if c_username and c_uid:
            request.session["username"]=c_username
            request.session["uid"]=c_uid
            # return HttpResponse("已经登录")
            return HttpResponseRedirect("/index/index")
        return render(request,"user/login.html")
    elif request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        try:
            user=User.objects.get(username=username)
        except Exception as e:
            print("--login user error %s"%(e))
            return HttpResponse("用户名或者密码错误")  #防黑客
        #比对密码
        m=hashlib.md5()
        m.update(password.encode())
        if m.hexdigest() != user.pass_word:
            return HttpResponse("用户名或者密码错误")
        
        # 记录会话状态
        request.session["username"] = username #当字典用
        request.session["uid"]=user.id

        # resp=HttpResponse("登录成功")
        resp=HttpResponseRedirect("/index/index")
        #判断是否选择了记住用户名  选了我就存3天
        if "remember" in request.POST:  #POST是一个列表，通过看浏览器请求的数据判断的 
            resp.set_cookie("username",username,3600*24*3)
            resp.set_cookie("uid",user.id,3600*24*3)
        return resp

def logout_view(request):
    #删除session
    if "username" in request.session:
        del request.session["username"]
    if "uid" in request.session:
        del request.session["uid"]
    
    resp=HttpResponseRedirect("/index/index")
    if "username" in request.COOKIES:
        resp.delete_cookie("username")
    if "uid" in request.COOKIES:
        resp.delete_cookie("uid")
    return resp




#测试文件上传
def test_upload(request):
    if request.method=="GET":
        return render(request,"user/test_upload.html")
    elif request.method=="POST":
        title =request.POST["title"]
        a_file=request.FILES["myfile"]
        Content.objects.create(title=title,picture=a_file)
        return HttpResponse("上传文件成功")



        
