from stark.service.v1 import site,StarkHandler
from app01 import models
from django.shortcuts import HttpResponse


class UserInfoHandler(StarkHandler):
    pass

class DepartHandler(StarkHandler):
    pass

site.register(models.UserInfo, UserInfoHandler)
site.register(models.Depart, DepartHandler)
models.UserInfo.objects.all()