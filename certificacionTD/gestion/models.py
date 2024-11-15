from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('empleado', 'Empleado'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='empleado')

# Client model
class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

# Garment model
class Prenda(models.Model):
    tipo_prenda = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.tipo_prenda} - ${self.precio}"

# Service Order model
class OrdenDeServicio(models.Model):
    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('completada', 'Completada'),
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'employee'})
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    prendas = models.ManyToManyField(Prenda)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    pago_realizado = models.BooleanField(default=False)

    def __str__(self):
        return f"Orden {self.id} - {self.cliente.nombre}"

    def calcular_total(self):
        total = sum([prenda.precio for prenda in self.prendas.all()])
        self.total = total
        self.save()

# Sale model
class Venta(models.Model):
    METODO_PAGO_CHOICES = (
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta de Crédito/Débito'),
        ('transferencia', 'Transferencia Bancaria'),
    )
    orden_servicio = models.OneToOneField(OrdenDeServicio, on_delete=models.CASCADE)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=50, choices=METODO_PAGO_CHOICES)

    def __str__(self):
        return f"Venta {self.id} - Orden {self.orden_servicio.id} - ${self.monto_total}"