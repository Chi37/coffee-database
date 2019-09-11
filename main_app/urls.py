from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('coffees/', views.index, name = 'coffees_index'),
    path('coffees/create/', views.CoffeeCreateView.as_view(), name='coffees_create'),
    path('coffees/<int:pk>', views.CoffeeDetailView.as_view(), name = 'detail'),
    path('coffees/<int:pk>/delete/', views.CoffeeDelete.as_view(), name='coffees_delete'),
    path('coffees/<int:pk>/update/', views.CoffeeUpdateView.as_view(), name='coffees_update'),
]