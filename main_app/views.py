from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Coffee



def home(request):
    return render(request, 'about.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    coffees = Coffee.objects.all()
    return render(request, 'coffees/index.html', { 'coffees': coffees })
    

class CoffeeDetailView(DetailView):
    model = Coffee
    def coffee_detail_view(request, primary_key):
        try:
            coffee = Coffee.objects.get(pk = primary_key)
        except Coffee.DoesNotExist:
            raise Http404('Coffee Does Not Exist')

        return render(request, 'coffees/detail.html', { 'coffee': coffee } )


class CoffeeCreateView(CreateView):
  model = Coffee
  fields = '__all__'

class CoffeeDeleteView(DeleteView):
    model = Coffee
    