from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),  # URL para ver la lista de productos
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
]
