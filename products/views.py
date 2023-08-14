from django.http import HttpResponse
from django.shortcuts import render
from .models import Products

def calculate():
    x = 1
    y = 2
    return x

def index(request):
    x = calculate()
    products = Products.objects.all()
    return render(request, 'index.html', 
                  {'products': products})