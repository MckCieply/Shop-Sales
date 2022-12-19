from django.shortcuts import render
from django.http import response

def home(response):
    return render(response, 'productsale/home.html')
