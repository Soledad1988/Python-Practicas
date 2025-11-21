#from django.views.generic import TemplateView

#class Indexview(TemplateView):
#    template_name = 'index.html'

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')