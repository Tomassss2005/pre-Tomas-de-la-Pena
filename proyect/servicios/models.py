from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    

    def __str__(self) -> str:
        return f"{self.nombre} ({self.apellido})"



class Servicio(models.Model):
    producto = models.CharField(max_length=50, unique=True)
    descripcion_producto = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.producto
    

class Pedido(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = "PENDIENTE", "Pendiente",
        EN_PROGRESO = "EN_PROGRESO", "En progreso",
        TERMINADO = "TERMINADO", "Terminado",
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    descripcion_pedido = models.TextField(blank=True, null=True)
    fecha_pedido = models.DateField(auto_now_add=True)
    fecha_entregado = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PENDIENTE)
    
def __str__(self) -> str:
        return f"Pedido de {self.servicio.nombre} para {self.usuario.nombre}"