from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
def index_view(request):
    # return HttpResponse("这是新闻频道首页")
    return render(request,"news/index.html")