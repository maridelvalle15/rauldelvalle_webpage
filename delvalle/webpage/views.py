from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'


class CV(TemplateView):
    template_name = 'cv.html'


class Interes(TemplateView):
    template_name = 'interes.html'
