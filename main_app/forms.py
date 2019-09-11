from django.forms import ModelForm
from .models import Method

class MethodForm(ModelForm):
  class Meta:
    model = Method
    fields = ['methods']


