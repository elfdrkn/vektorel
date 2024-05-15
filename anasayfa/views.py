from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def anasayfa(request):
    return HttpResponse("Ana sayfaya hoş geldiniz.")

def xxxen(request):
  return HttpResponse("Welcome my website.")

from django.template import loader
def anasayfa(request):
  template = loader.get_template('ana.html')
  return HttpResponse(template.render())


