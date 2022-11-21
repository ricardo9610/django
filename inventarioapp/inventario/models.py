from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    nivel = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    fecha = models.DateTimeField("fecha de modificacion")
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
