from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
    
    
class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.TextField()
    telefono = models.TextField()

    def __str__(self):
        return self.nombre
    

class Pedidos(models.Model):
    clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    fecha_pedidos = models.DateField(auto_now_add=True) 

    def __str__(self):
        return self.fecha_pedidos
    
class Ventas(models.Model):
    pedidos = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fecha
    
    
