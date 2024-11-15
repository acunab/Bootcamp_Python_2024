# core/forms.py
from django import forms
from .models import Cliente, OrdenDeServicio, Prenda, Venta
from django.contrib.auth import get_user_model

User = get_user_model()

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'correo', 'direccion']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'role']

class PrendaForm(forms.ModelForm):
    class Meta:
        model = Prenda
        fields = ['tipo_prenda', 'precio', 'descripcion']

class OrdenForm(forms.ModelForm):
    class Meta:
        model = OrdenDeServicio
        fields = ['cliente', 'empleado', 'prendas']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['metodo_pago']
