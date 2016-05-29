from django.views.generic import TemplateView


class Rekt(TemplateView):
    template_name = "rekt.html"

    def get_context_data(self, **kwargs):
        ctx = super(Rekt, self).get_context_data(**kwargs)
        ctx['something_else'] = None  # add something to ctx
        return ctx
