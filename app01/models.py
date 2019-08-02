from django.db import models


# Create your models here.

class Depart(models.Model):
    '''
    部门表
    '''
    title = models.CharField(verbose_name='部门名称', max_length=32)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    '''
    用户表
    '''
    name = models.CharField(verbose_name='姓名', max_length=32)
    age = models.IntegerField()
    email = models.EmailField(verbose_name='邮箱', max_length=32)
    depart = models.ForeignKey(to='Depart', verbose_name='部门')

    def __str__(self):
        return self.name