from django.conf.urls import url

from ProjectManagment.modules.admin.views.index import Index


def getModuleUrls():
    return [
        url(r'^$', Index.as_view(), name='index')
    ]
