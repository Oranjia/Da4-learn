import email
from tabnanny import verbose
from django.db import models
from matplotlib.cbook import print_cycles
from matplotlib.pyplot import title

# Create your models here.
class Book(models.Model):
    title=models.CharField("书名",max_length=50,default="") #"书名"是verbose_name的属性，就是在admin后台显示的名字
    pub=models.CharField("出版社",max_length=100,default="")
    price=models.DecimalField("价格",max_digits=7,decimal_places=2)  #总位数7，小数点位数2
    market=models.DecimalField("零售价",max_digits=7,decimal_places=2,default=0.0)
    is_active=models.BooleanField("是否活跃",default=True)
    class Meta:
        db_table="book"   #可以把当前模型类的表名字改成book
        verbose_name="图书"  #把admin页面的表的名字改掉
        verbose_name_plural=verbose_name  #去掉s
    def __str__(self):   #方便后面的可视化  两个下划线
        return "%s_%s_%s_%s"%(self.title,self.pub,self.price,self.market)

class Author(models.Model):
    name=models.CharField("姓名",max_length=11)
    age=models.IntegerField("年龄",default=1)
    email=models.EmailField("邮箱",null=True)

    class Meta:
        db_table="author"
