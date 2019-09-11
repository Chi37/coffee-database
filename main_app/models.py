from django.db import models
from django.urls import reverse

class Coffee(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'pk': self.id}) 

