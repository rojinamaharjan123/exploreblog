from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.urls import reverse_lazy

# Create your views here.
class HomeView(TemplateView):
	template_name = "clienttemplates/clienthome.html"
