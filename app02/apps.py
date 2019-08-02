from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules

class App02Config(AppConfig):
    name = 'app02'

    def ready(self):
        return autodiscover_modules('stark')