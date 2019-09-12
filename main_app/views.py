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
    

# class CoffeeDetailView(DetailView):
# 	model = Coffee
# 	method_form = MethodForm()


def coffees_detail(request, coffee_id):
	coffee = Coffee.objects.get(id=coffee_id)
	method_form = MethodForm()
	return render(request, 'coffees/detail.html', {
    # pass the coffee and feeding_form as context
    'coffee': coffee, 
		'method_form': method_form,
  })

def add_method(request, coffee_id):
	# create the ModelForm using the data in request.POST
  form = MethodForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
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