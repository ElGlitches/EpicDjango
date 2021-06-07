from django.contrib import admin
from EpicPro.models import Clientes,Juegos,Pedidos,contacto
from .forms import JuegosForm

# Register your models here.
#muestra nombres, y campo de busqueda
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","tel")
    search_fields=("nombre", "tel")

#filtra por nombre y precio
class JuegosAdmin(admin.ModelAdmin):
    list_display=("nombre","precio","codigo")
    list_filter=("nombre","precio",)
    form = JuegosForm


class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha","entregado")
    list_filter=("fecha",)
    date_hierarchy="fecha"

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Juegos,JuegosAdmin)
admin.site.register(Pedidos,PedidosAdmin)
admin.site.register(contacto)

