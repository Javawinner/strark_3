# (urlconf_module, app_name, namespace)
from django.conf.urls import url
from django.shortcuts import HttpResponse, render


class StarkSite(object):
    def __init__(self):
        self.app_name = 'stark'
        self.namespace = 'stark'
        self._registery = []

    def register(self, model_class, handler_class):
        return self._registery.append({'model_class': model_class, 'handler_class': handler_class(model_class)})

    @property
    def get_url(self):
        patterns = []
        '''
        测试： patterns.append(url(r'^x1/$', lambda request: HttpResponse('test')))
        '''
        for item in self._registery:
            model_class = item['model_class']
            handler_class = item['handler_class']
            # /app01/depart/list  /app01/depart/add  /app01/depart/edit/1  /app01/depart/del/1
            # 拿到应用名
            app_label = model_class._meta.app_label
            model_name = model_class._meta.model_name

            patterns.append(url(r'^%s/%s/list' % (app_label, model_name), handler_class.Chang_list))
            patterns.append(url(r'^%s/%s/add' % (app_label, model_name), handler_class.add_view))
            patterns.append(url(r'^%s/%s/edit/(\d+)' % (app_label, model_name), handler_class.change_view))
            patterns.append(url(r'^%s/%s/del/[0-9]+' % (app_label, model_name), handler_class.delete_view))

        return patterns

    @property
    def urls(self):
        return self.get_url, self.app_name, self.namespace


class StarkHandler(object):
    def __init__(self, model_class):
        self.model_class = model_class

    def Chang_list(self, request):
        '''
        查看页面
        :param request:
        :return:
        '''
        print(self.model_class)
        data_list = self.model_class.objects.all()
        return render(request, 'stark/changelist.html', {'data_list': data_list})

    def add_view(self, request):
        '''
        添加页面
        :param request:
        :return:
        '''
        return HttpResponse('添加页面')

    def change_view(self, request, pk):
        '''
        编辑页面
        :param request:
        :param pk:
        :return:
        '''
        return HttpResponse('编辑页面')

    def delete_view(self, request, pk):
        '''
        删除页面
        :param request:
        :param pk:
        :return:
        '''
        return HttpResponse('删除页面')


site = StarkSite()
