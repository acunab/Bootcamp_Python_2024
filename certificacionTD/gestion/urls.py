# gestion/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('registro-cliente/', views.registro_cliente, name='registro_cliente'),
    path('alta-empleado/', views.alta_empleado, name='alta_empleado'),
    path('gestion-prendas/', views.gestion_prendas, name='gestion_prendas'),
    path('agregar-prenda/', views.agregar_prenda, name='agregar_prenda'),
    path('generar-orden/', views.generar_orden, name='generar_orden'),
    path('seguimiento-ordenes/', views.seguimiento_ordenes, name='seguimiento_ordenes'),
    path('actualizar-estado-orden/<int:pk>/', views.actualizar_estado_orden, name='actualizar_estado_orden'),
    path('cobrar-orden/<int:pk>/', views.cobrar_orden, name='cobrar_orden'),
    path('reporte-ventas/', views.reporte_ventas, name='reporte_ventas'),
]