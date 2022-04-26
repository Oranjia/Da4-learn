from unicodedata import name
from django.db import models
from matplotlib.pyplot import title

# Create your models here.

#一对一
class Author (models.Model):
    #有一个反向的属性wife
    name=models.CharField("姓名",max_length=11)

class Wife(models.Model):
    name=models.CharField("姓名",max_length=11)
    author=models.OneToOneField(Author,on_delete=models.CASCADE)  #关联的author的主键作为外键


#一对多
class Publisher(models.Model):
    #book_set属性隐藏的
    name=models.CharField("出版社名称",max_length=50)

class Book(models.Model):
    title=models.CharField("书名",max_length=11)
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)  #多

"""
有属性的查没有属性的是正向查询
book.publisher
abook=Book.objects.get(id=1)
print(abook.tittle,"的出版社是：",abook.publisher.name)

反向查询
pub1=Publisher.objects.get(name="北京大学出版社")
books=pub1.book_set.all()  #或者使用books=Book.objects.filter(publisher=pub1)

"""


#多对多
# 一个作者多本书，一本书多个作者
class Authors(models.Model):
    name=models.CharField("姓名",max_length=11)

class Books(models.Model):
    title=models.CharField("书名",max_length=11)
    authors=models.ManyToManyField(Author)


"""
a1=Authors.objects.create(name="guolaoshi")
b1=a1.books_set.create(title="Python1")   #对应类小写_set

a2=Authors.objects.create(name="chenlaoshi")
a2.books_set.add(b1)


...这里有点问题，和上面的Author的class关联了


对于查询，book.author.all()

"""