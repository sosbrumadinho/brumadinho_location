from django.views.generic import TemplateView


class ViewMap(TemplateView):
    template_name = 'index.html'


viewmap = ViewMap.as_view()
