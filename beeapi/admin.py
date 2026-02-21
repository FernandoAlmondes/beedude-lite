from django.contrib import admin
from .models import Servidor, Mapa, Node, Edge
# Register your models here.

class ServidorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'url', 'status']
    list_filter = ['status']
    search_fields = ['nome', 'url']
admin.site.register(Servidor, ServidorAdmin)

class MapaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'servidor', 'status', 'default']
    list_filter = ['status']
    search_fields = ['nome', 'servidor']
admin.site.register(Mapa, MapaAdmin)

class NodeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'x', 'y', 'icone', 'classe', 'mapa__nome', 'mapa__servidor']
    list_filter = ['mapa']
    search_fields = ['nome']
admin.site.register(Node, NodeAdmin)

class EdgeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'source', 'target', 'mapa__nome', 'mapa__servidor']
    list_filter = ['mapa']
    search_fields = ['nome', 'source', 'target']
admin.site.register(Edge, EdgeAdmin)