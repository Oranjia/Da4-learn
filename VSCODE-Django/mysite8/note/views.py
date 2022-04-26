from tabnanny import check
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from matplotlib.pyplot import title
from .models import Note

# Create your views here.
#检查登录状态
def check_login(fn): #外层的参数是包裹的函数 视图函数
    def wrap(request,*args,**kwargs): #里面的参数就是视图函数的参数
        if "username" not in request.session or "uid" not in request.session:
            #检查cookie
            c_username=request.COOKIES.get("username")
            c_uid=request.COOKIES.get("uid")
            if not c_username or c_uid:
                return HttpResponseRedirect("/user/login")
            else:
                #回写session
                request.session["username"]=c_username
                request.session["uid"]=c_uid
        return fn(request,*args,**kwargs)
    return wrap

@check_login 
def add_note(request):
    if request.method=="GET":
        return render(request,"note/add_note.html")
    
    elif request.method=="POST":
        uid=request.session["uid"]
        title=request.POST["title"]
        content=request.POST["content"]
        Note.objects.create(title=title,content=content,user_id=uid)
        return HttpResponse("添加笔记成功")