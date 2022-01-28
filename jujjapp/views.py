from django.shortcuts import render
from django.views import generic
from .models import Project

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'jujjapp/detail.html'
    model = Project
