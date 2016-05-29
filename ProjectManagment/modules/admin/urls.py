from django.conf.urls import url

from ProjectManagment.modules.admin.views.index import Index
from ProjectManagment.modules.admin.views.rekt import Rekt


def getModuleUrls():
    return [
        url(r'^$', Index.as_view(), name='index'),
        url(r'^rekt/$', Rekt.as_view(), name="rekt")
    ]
