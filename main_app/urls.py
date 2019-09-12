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
    path('coffees/<int:coffee_id>/assoc_store/<int:store_id>/', views.assoc_store, name='assoc_store'),
    path('stores/', views.StoreListView.as_view(), name='stores_index'),
    path('stores/create', views.StoreCreateView.as_view(), name='stores_create'),
    path('stores/<int:pk>/', views.StoreDetailView.as_view(), name='stores_detail'),
    path('stores/<int:pk>/update/', views.StoreUpdateView.as_view(), name='stores_update'),
]


#   path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
#   path('coffee/<int:cat_id>/assoc_toy/<int:toy_id>/delete', views.delete_assoc_toy, name='delete_assoc_toy'),