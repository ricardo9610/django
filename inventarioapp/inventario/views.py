from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Producto

def index(request):
    latest_producto_list = Producto.objects.all()
    return render(request , "inventario/index.html", {
        "latest_producto_list": latest_producto_list
    })


def login(request):
    return HttpResponse(f"inicio de secion ")

def registro(request):
    return HttpResponse(f"Registro")

def lista(request,producto_id):
    return HttpResponse(f"Lista de Productos")

def editar(request,producto_id):
    producto = get_object_or_404(Producto, pk = producto_id)
    return render(request,"inventario/editar.html",{
        "producto": producto
    } )
