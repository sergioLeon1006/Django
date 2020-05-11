from django.contrib import admin
from .models import Roles,DatosUser,Habilidades,Rates,DetaRoles
# Register your models here.
class RolModel(admin.ModelAdmin):
    list_display =["Roles"]
    list_display_links =["Roles"]
    list_filter = ["Roles"]
    class Meta:
        model=Roles
admin.site.register(Roles)
class DatosUserModel(admin.ModelAdmin):
    list_display =["DatosUSer"]
    list_display_links =["DatosUSer"]
    list_filter = ["DatosUser"]
    class Meta:
        model = DatosUser
admin.site.register(DatosUser)
class HabilidadesModel(admin.ModelAdmin):
    list_display =["Habilidades"]
    list_display_links =["Habilidades"]
    list_filter = ["Habilidades"]
    class Meta:
        model =Habilidades
admin.site.register(Habilidades)
class RatesModel(admin.ModelAdmin):
    list_display =["Rates"]
    list_display_links =["Rates"]
    list_filter = ["Rates"]
    class Meta:
        model= Rates
admin.site.register(Rates)
class DetaRolesModel(admin.ModelAdmin):
    list_display =["DetaRoles"]
    list_display_links =["DetaRoles"]
    list_filter = ["DetaRoles"]
    class Meta:
        model= DetaRoles
admin.site.register(DetaRoles)