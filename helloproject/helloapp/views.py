from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class HelloView(TemplateView):
    template_name = "hello.html"