from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('coffees/', views.index, name = 'coffees_index'),
    path('coffees/create/', views.CoffeeCreateView.as_view(), name='coffees_create'),
    path('coffees/<int:coffee_id>/', views.coffees_detail, name = 'detail'),
    path('coffees/<int:coffee_id>/add_method/', views.add_method, name = 'add_method'),
    path('coffees/<int:pk>/delete/', views.CoffeeDelete.as_view(), name='coffees_delete'),
    path('coffees/<int:pk>/update/', views.CoffeeUpdateView.as_view(), name='coffees_update'),
    path('stores/', views.StoreListView.as_view(), name='stores_index'),
    path('stores/create', views.StoreCreateView.as_view(), name='stores_create'),
    path('stores/<int:pk>/', views.StoreDetailView.as_view(), name='stores_detail'),
]


#   path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
#   path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
#   path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
