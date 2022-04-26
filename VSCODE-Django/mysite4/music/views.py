from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index_view(request):
    # return HttpResponse("这是音乐频道首页")
    return render(request,"index.html")