from unicodedata import name
from operator import index
from django.urls import path , include
from .import views
from django.views.generic import TemplateView

urlpatterns = [

    path('', TemplateView.as_view(template_name= 'myprofile.html'))
]