from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from DetailApp.models import  AppDetail

def  DetailApp(request):
    # if  request.user.is_authenticated:
    return HttpResponsePermanentRedirect("/cli/HomePage/")



