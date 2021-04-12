from django.shortcuts import render
from django.http import HttpResponse

def todoapp(request):
  return HttpResponse('Hello Django!')
  
# Create your views here.
