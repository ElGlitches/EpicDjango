from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50, blank=True,null=True)
    email=models.EmailField()
    tel=models.CharField(max_length=9, blank=True,null=True)
    
    # Para ver el nombre del cliente
    def __str__(self):
        return self.nombre

class Juegos(models.Model):
    nombre=models.CharField(max_length=30)
    codigo=models.IntegerField()
    precio=models.IntegerField()

    imagen = models.ImageField(upload_to="juegos", null=True)

    def __str__(self):
        return self.nombre

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

opciones_consultas =[
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]
class contacto(models.Model):
    nombre=models.CharField(max_length=50)
    correo=models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje =models.TextField()
    avisos = models.BooleanField()

    
    def __str__(self):
        return self.nombre
