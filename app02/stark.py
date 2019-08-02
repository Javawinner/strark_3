from stark.service.v1 import site,StarkHandler
from app02 import models
from django.shortcuts import HttpResponse

class HostHandler(StarkHandler):
    pass


class RoleHandler(StarkHandler):
    pass

class ProjectHandler(StarkHandler):
    pass

site.register(models.Host, HostHandler)
site.register(models.Role, RoleHandler)
site.register(models.Project,ProjectHandler)