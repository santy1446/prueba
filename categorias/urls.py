from django.urls import path

from . import views

urlpatterns = [
    path('listar/', views.categorias_listar, name='listar')
]
