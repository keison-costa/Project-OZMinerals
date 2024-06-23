from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import LinhaTelefonica, Aparelhos

####################################################################################################################

class LinhaTelefonicaResource(resources.ModelResource):
    class Meta:
        model = LinhaTelefonica

class LinhaTelefonicaAdmin(ImportExportModelAdmin):
    resource_class = LinhaTelefonicaResource
    list_display = ('imei_number', 'telefone', 'user', 'registration_datetime')
    search_fields = ('imei_number', 'telefone', 'user__UTILIZADOR')
    list_filter = ('registration_datetime',)

admin.site.register(LinhaTelefonica, LinhaTelefonicaAdmin)

####################################################################################################################

class AparelhosResource(resources.ModelResource):
    class Meta:
        model = Aparelhos

class AparelhosAdmin(ImportExportModelAdmin):
    resource_class = AparelhosResource
    list_display = ('IMEI_APARELHO', 'MODELO', 'FABRICANTE', 'UTILIZADOR', 'EMAIL', 'LOGIN_ADMANAGER')
    search_fields = ('IMEI_APARELHO', 'MODELO', 'FABRICANTE', 'UTILIZADOR', 'EMAIL', 'LOGIN_ADMANAGER')
    list_filter = ('IMEI_APARELHO', 'MODELO', 'FABRICANTE', 'UTILIZADOR', 'EMAIL', 'LOGIN_ADMANAGER')

admin.site.register(Aparelhos, AparelhosAdmin)

####################################################################################################################
