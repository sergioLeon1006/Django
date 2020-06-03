from django.contrib import admin
from .models import CategoriaProyecto,TipoDocu,Proyecto,Documento
# Register your models here.
class CategoriaModel(admin.ModelAdmin):
    list_display = ["Categoria"]
    list_display_links = ["Categoria"]
    list_filter = ["Categoria"]
    class Meta:
        model = CategoriaProyecto
admin.site.register(CategoriaProyecto)
class TipoDocuModel(admin.ModelAdmin):
    list_display = ["TipoDocumento"]
    list_display_links = ["TipoDocumento"]
    list_filter = ["TipoDocumento"]
    class Meta:
        model = TipoDocu
admin.site.register(TipoDocu)
class ProyectoModel(admin.ModelAdmin):
    list_display = ["Proyecto"]
    list_display_links = ["Proyecto"]
    list_filter = ["Proyecto"]
    class Meta:
        model = Proyecto
admin.site.register(Proyecto)
class DocumentoModel(admin.ModelAdmin):
    list_display = ["Documento"]
    list_display_links = ["Documento"]
    list_filter = ["Documento"]
admin.site.register(Documento)