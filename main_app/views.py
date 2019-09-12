from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Coffee, Store
from .forms import MethodForm


def home(request):
	return render(request, 'about.html')

def about(request):
	return render(request, 'about.html')

def index(request):
	coffees = Coffee.objects.all()
	return render(request, 'coffees/index.html', { 'coffees': coffees })
    
def coffees_detail(request, coffee_id):
	coffee = Coffee.objects.get(id=coffee_id)
	method_form = MethodForm()
	return render(request, 'coffees/detail.html', {
    'coffee': coffee, 
		'method_form': method_form,
  })

def add_method(request, coffee_id):
  form = MethodForm(request.POST)
  if form.is_valid():
    new_method = form.save(commit=False)
    new_method.coffee_id = coffee_id
    new_method.save()
  return redirect('detail', coffee_id=coffee_id)


class CoffeeCreateView(CreateView):
    model = Coffee
    fields = '__all__'

class CoffeeDelete(DeleteView):
    model = Coffee
    success_url = '/coffees/'

class CoffeeUpdateView(UpdateView):
	model = Coffee
	fields = ['region','description']


class StoreListView(ListView):
	model = Store

class StoreCreateView(CreateView):
	model = Store
	fields = '__all__'

class StoreDetailView(DetailView):
	model = Store
	fields = '__all__'


class StoreUpdateView(UpdateView):
	model = Store
	fields = '__all__'

def assoc_store(request, coffee_id, store_id):
	Coffee.objects.get(id=coffee_id).stores.add(store_id)
	return redirect('detail', coffee_id=coffee_id)
