from django.forms import ModelForm
from .models import Method, Store

class MethodForm(ModelForm):
  class Meta:
    model = Method
    fields = ['methods']

class StoreForm(ModelForm):
    model = Store
    fields = '__all__'


