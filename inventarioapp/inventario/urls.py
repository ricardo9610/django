from django.urls import path

from . import views

app_name="inventario"

urlpatterns = [
    path("" ,views.index , name="index"),
    path("<int:producto_id>/" ,views.editar , name="editar"),
    path("login/" ,views.login , name="index"),
    path("registro/" ,views.registro , name="index"),
    path("lista/" ,views.lista , name="index")
    
]