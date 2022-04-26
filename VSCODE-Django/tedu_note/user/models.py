from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField("用户名",max_length=50)
    pass_word=models.CharField("密码",max_length=20)
    created_time=models.DateTimeField("创建时间",auto_now_add=True)
    updated_time=models.DateTimeField("更新时间",auto_now=True)

    def __str__(self):
        return "username %s"%(self.username)