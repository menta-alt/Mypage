from django.db import models


# Create your models here.
class User(models.Model):
    user_type_choices = (
        (1,'普通用户'),
        (2,'VIP用户'),
        (3,'SVIP用户')
    )
    #账号
    username=models.CharField(max_length=200 ,blank=True,null=True)
    #密码
    password=models.CharField(max_length=200,blank=True,null=True)

    usertype = models.IntegerField(choices = user_type_choices,null=True)

    objects = models.Manager()
    DoesNotExist = models.Manager()

from django.contrib import admin
admin.site.register(User)