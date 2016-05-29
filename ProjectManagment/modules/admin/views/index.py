from django.views.generic import TemplateView
from ProjectManagment.modules.admin.library.admin import Admin
from django.http import HttpResponse
from django.shortcuts import render


class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        ctx = super(Index, self).get_context_data(**kwargs)
        ctx['something_else'] = None  # add something to ctx
        return ctx

    # def get(self, request, *args, **kwargs):
    #     return render(self, self.template_name, HttpResponse(admin.sampleMethod(5, 5)))
