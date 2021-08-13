from django.shortcuts import render
from django.http import HttpResponse as htr
# Create your views here.
def display(show):
    
    return htr("Hi welcome to django")
    
def home(request):
    return htr("<h1>Welcome to home page</h1>")
        