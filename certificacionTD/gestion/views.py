# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib.auth import get_user_model
from .models import Cliente, Prenda, OrdenDeServicio, Venta
from .forms import ClienteForm, EmpleadoForm, OrdenForm, PrendaForm, VentaForm

User = get_user_model()

# Registro de nuevos clientes
@login_required
def registro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'core/registro_cliente.html', {'form': form})

# Alta de empleados (administrador)
@login_required
def alta_empleado(request):
    if request.user.role == 'admin':
        if request.method == 'POST':
            form = EmpleadoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_empleados')
        else:
            form = EmpleadoForm()
        return render(request, 'core/alta_empleado.html', {'form': form})
    else:
        return redirect('no_autorizado')

# Gestión de prendas
@login_required
def gestion_prendas(request):
    prendas = Prenda.objects.all()
    return render(request, 'core/gestion_prendas.html', {'prendas': prendas})

@login_required
def agregar_prenda(request):
    if request.method == 'POST':
        form = PrendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion_prendas')
    else:
        form = PrendaForm()
    return render(request, 'core/agregar_prenda.html', {'form': form})

# Generación de órdenes de servicio
@login_required
def generar_orden(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            orden = form.save()
            orden.calcular_total()
            return redirect('seguimiento_ordenes')
    else:
        form = OrdenForm()
    return render(request, 'core/generar_orden.html', {'form': form})

# Seguimiento de órdenes
@login_required
def seguimiento_ordenes(request):
    ordenes = OrdenDeServicio.objects.all()
    return render(request, 'core/seguimiento_ordenes.html', {'ordenes': ordenes})

@login_required
def actualizar_estado_orden(request, pk):
    orden = get_object_or_404(OrdenDeServicio, pk=pk)
    if request.method == 'POST':
        orden.estado = request.POST.get('estado')
        orden.save()
        return redirect('seguimiento_ordenes')
    return render(request, 'core/actualizar_estado_orden.html', {'orden': orden})

# Cobro de órdenes de servicio
@login_required
def cobrar_orden(request, pk):
    orden = get_object_or_404(OrdenDeServicio, pk=pk)
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.orden_servicio = orden
            venta.monto_total = orden.total
            venta.save()
            orden.pago_realizado = True
            orden.save()
            return redirect('reporte_ventas')
    else:
        form = VentaForm()
    return render(request, 'core/cobrar_orden.html', {'form': form, 'orden': orden})

# Reporte de ventas
@login_required
def reporte_ventas(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    if fecha_inicio and fecha_fin:
        ventas = Venta.objects.filter(fecha_venta__range=[fecha_inicio, fecha_fin])
    else:
        ventas = Venta.objects.all()

    total_ventas = ventas.aggregate(Sum('monto_total'))['monto_total__sum']
    return render(request, 'core/reporte_ventas.html', {'ventas': ventas, 'total_ventas': total_ventas})