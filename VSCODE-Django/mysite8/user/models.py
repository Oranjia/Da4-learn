from django.db import models
from matplotlib.pyplot import title

# Create your models here.
class User(models.Model):
    username=models.CharField("用户名",max_length=50)
    pass_word=models.CharField("密码",max_length=20)
    created_time=models.DateTimeField("创建时间",auto_now_add=True)
    updated_time=models.DateTimeField("更新时间",auto_now=True)

    def __str__(self):
        return "username %s"%(self.username)


#上传用的
class Content(models.Model):
    title=models.CharField("文章名字",max_length=11)
    picture=models.FileField(upload_to="picture")