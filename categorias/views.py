from django.shortcuts import render

# Create your views here.
def categorias_listar(request):
    return  render(request, 'categorias/listar.html')
