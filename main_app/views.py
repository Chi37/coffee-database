from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('hello')

def about(request):
    return render(request, 'about.html')

def coffees_index(request):
    return HttpResponse('this is the index')
    



