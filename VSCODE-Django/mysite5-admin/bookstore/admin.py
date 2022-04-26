from django.contrib import admin
from .models import Book,Author #导入进来，为了让在admin后台能看到Book
# Register your models here.
class BookManage(admin.ModelAdmin):
    list_display=["id","title","pub","price"]
    list_display_links=["title"]  #把修改数据的超链接夹在title上面
    list_filter=["pub"] #添加过滤器，进行分类查询
    search_fields=["title"] #添加搜索框进行模糊查询
    list_editable=["price"] #和超链接互斥，然后可以在列表列直接编辑

class Author_Manage(admin.ModelAdmin):
    list_display=["id","name","age"]

admin.site.register(Book,BookManage)
admin.site.register(Author,Author_Manage)


