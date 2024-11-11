from django import forms
from .models import Reserva, Pedido, ItemPedido

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente', 'mesa', 'fecha_reserva', 'estado']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['reserva', 'cliente', 'total', 'estado', 'metodo_pago']

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['pedido', 'producto', 'cantidad', 'precio_unitario']