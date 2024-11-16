from django.shortcuts import render
from django.views import generic

def index(request):
    return render(request, 'index.html')

class login_view(generic.TemplateView):
    template_name = 'polls/login.html'

class BaseView(generic.TemplateView):
    template_name = 'polls/base.html'
