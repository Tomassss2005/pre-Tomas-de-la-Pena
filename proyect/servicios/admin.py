from django.contrib import admin

from .models import Usuario, Servicio, Pedido


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido')
    search_fields = ('nombre', 'apellido')
    ordering = ('nombre', 'apellido')

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'precio', 'estado')
    list_filter = ('estado',)
    search_fields = ('producto',)
    ordering = ('producto',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'servicio', 'fecha_pedido', 'fecha_entregado', 'estado')
    list_filter = ('fecha_pedido', 'estado')
    search_fields = ('usuario__nombre', 'servicio__nombre')
    ordering = ('-fecha_entregado',)
    date_hierarchy = 'fecha_pedido'