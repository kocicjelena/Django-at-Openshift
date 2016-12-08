import os
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import Http404, HttpResponse
from django.views.generic import TemplateView
from django.views.generic import View
def home(request):
    return render_to_response('home/home.html')
def index(request):
    return HttpResponse("<a href='/posts'>Blog</a>")