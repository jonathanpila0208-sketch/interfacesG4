from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    apellido_cliente = models.CharField(max_length=100)
    cedula_cliente = models.CharField(max_length=10)
    telefono_cliente = models.CharField(max_length=15)
    direccion_cliente = models.CharField(max_length=255)
    estado_cliente = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre_cliente} {self.apellido_cliente}"