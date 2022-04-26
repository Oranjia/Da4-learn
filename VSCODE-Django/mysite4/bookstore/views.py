from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Book
# Create your views here.

def all_book(request):
    #all_book=Book.objects.all()
    all_book=Book.objects.filter(is_active=True)
    return render(request,"bookstore/all_book.html",locals())

def update_book(request,book_id):
    try:
        book=Book.objects.get(id=book_id,is_active=True)
    except Exception as e:
        print("--ipdate book error is %s"%(e))
        return HttpResponse("这本书不存在")

    if request.method=="GET":
        return render(request,"bookstore/update_book.html",locals())
    
    elif request.method=="POST":
        price=request.POST["price"]
        market=request.POST["market"]
        #改
        book.price=price
        book.market=market
        #保存
        book.save()
        return HttpResponseRedirect("/bookstore/all_book")

def delete_book(request):
    book_id=request.GET.get("book_id")
    if not book_id:
        return HttpResponse("---请求异常")
    try:
        book=Book.objects.get(id=book_id,is_active=True)
    except Exception as e:
        print("---delete book get error %s" %(e))
        return HttpResponse("book id is error")
    
    book.is_active=False   #伪删除
    book.save()
    return HttpResponseRedirect("/bookstore/all_book")
