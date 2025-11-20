from django.views.generic import TemplateView

class Indexview(TemplateView):
    template_name = 'index.html'