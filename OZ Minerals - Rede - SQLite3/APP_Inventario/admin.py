from django.contrib import admin
from .models import PEDRABRANCA
from .models import CAN
from .models import Message
from .models import VLANs
from .models import BHZ
from .models import ROUTES
from .models import CAMERAS
from .models import PANTERA
from .models import ACSSES_POINT
from .models import MATERIAL
from .models import ANTAS_NORTE
from .models import EXTERNAL_IPS
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import ativosgeral

###########################################################################################################################################

from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .resources import UserResource, GroupResource, MakeMessagesResource
from .models import MakeMessages

# Desregistre o modelo User padrão
admin.site.unregister(User)

# Registre o modelo User com a nova configuração
@admin.register(User)
class UserAdmin(ImportExportModelAdmin, DefaultUserAdmin):
    resource_class = UserResource

# Desregistre o modelo Group padrão
admin.site.unregister(Group)

# Registre o modelo Group com a nova configuração
@admin.register(Group)
class GroupAdmin(ImportExportModelAdmin):
    resource_class = GroupResource

# Registre o modelo MakeMessages com a nova configuração
@admin.register(MakeMessages)
class MakeMessagesAdmin(ImportExportModelAdmin):
    resource_class = MakeMessagesResource

###########################################################################################################################################

class CAMERASResource(resources.ModelResource):
    class Meta:
        model = CAMERAS
class CAMERASAdmin(ImportExportModelAdmin):
    resource_class = CAMERASResource
    list_display = ('IP_ADDRESS', 'N_CANAL', 'PORTA', 'DISPOSITIVO_ID_CLOUD', 'FABRICANTE', 'MODELO', 'ADOTADO_EM', 'LOCAL', 'OBS',)
    search_fields = ('IP_ADDRESS', 'N_CANAL', 'PORTA', 'DISPOSITIVO_ID_CLOUD', 'FABRICANTE', 'MODELO', 'ADOTADO_EM', 'LOCAL', 'OBS',)
    list_filter = ('IP_ADDRESS', 'N_CANAL', 'PORTA', 'DISPOSITIVO_ID_CLOUD', 'FABRICANTE', 'MODELO', 'ADOTADO_EM', 'LOCAL', 'OBS',)
admin.site.register(CAMERAS, CAMERASAdmin)

###########################################################################################################################################

class ativosgeralResource(resources.ModelResource):
    class Meta:
        model = ativosgeral
class ativosgeralAdmin(ImportExportModelAdmin):
    resource_class = ativosgeralResource
    list_display = ('hostname', 'vlan', 'ip', 'mac', 'nserie', 'fabricante', 'modelo', 'instaladoem', 'localidade', 'categoria', 'tipo', 'tipogestao', 'criado_em', 'atualizado_em', 'usuario', 'senha',)
    search_fields = ('hostname', 'vlan', 'ip', 'mac', 'nserie', 'fabricante', 'modelo', 'instaladoem', 'localidade', 'categoria', 'tipo', 'tipogestao', 'criado_em', 'atualizado_em', 'usuario', 'senha',)
    list_filter = ('hostname', 'vlan', 'ip', 'mac', 'nserie', 'fabricante', 'modelo', 'instaladoem', 'localidade', 'categoria', 'tipo', 'tipogestao', 'criado_em', 'atualizado_em', 'usuario', 'senha',)
admin.site.register(ativosgeral, ativosgeralAdmin)

###########################################################################################################################################

class ACSSES_POINTResource(resources.ModelResource):
    class Meta:
        model = ACSSES_POINT
class ACSSES_POINTAdmin(ImportExportModelAdmin):
    resource_class = ACSSES_POINTResource
    list_display = ('hostname', 'sitecontroller', 'ip', 'mac', 'vlan', 'modelo', 'fabricante', 'instaladoem', 'localidade', 'tipo',)
    search_fields = ('hostname', 'sitecontroller', 'ip', 'mac', 'vlan', 'modelo', 'fabricante', 'instaladoem', 'localidade', 'tipo',)
    list_filter = ('hostname', 'sitecontroller', 'ip', 'mac', 'vlan', 'modelo', 'fabricante', 'instaladoem', 'localidade', 'tipo',)
admin.site.register(ACSSES_POINT, ACSSES_POINTAdmin)

###########################################################################################################################################

class ROUTESResource(resources.ModelResource):
    class Meta:
        model = ROUTES
class ROUTESAdmin(ImportExportModelAdmin):
    resource_class = ROUTESResource
    list_display = ('VLAN01', 'NAME', 'VLAN02', 'VLAN_10', 'VLAN_20', 'VLAN_30', 'VLAN_31', 'VLAN_32', 'VLAN_42', 'VLAN_44', 'VLAN_132', 'VLAN_224', 'VLAN_226', 'VLAN_228', 'VLAN_236', 'VLAN_250', 'VLAN_251', 'INTERNET', 'COMENTARIOS',)
    search_fields = ('VLAN01', 'NAME', 'VLAN02', 'VLAN_10', 'VLAN_20', 'VLAN_30', 'VLAN_31', 'VLAN_32', 'VLAN_42', 'VLAN_44', 'VLAN_132', 'VLAN_224', 'VLAN_226', 'VLAN_228', 'VLAN_236', 'VLAN_250', 'VLAN_251', 'INTERNET', 'COMENTARIOS',)
    list_filter = ('VLAN01', 'NAME', 'VLAN02', 'VLAN_10', 'VLAN_20', 'VLAN_30', 'VLAN_31', 'VLAN_32', 'VLAN_42', 'VLAN_44', 'VLAN_132', 'VLAN_224', 'VLAN_226', 'VLAN_228', 'VLAN_236', 'VLAN_250', 'VLAN_251', 'INTERNET', 'COMENTARIOS',)
admin.site.register(ROUTES, ROUTESAdmin)

###########################################################################################################################################

class ANTAS_NORTEResource(resources.ModelResource):
    class Meta:
        model = ANTAS_NORTE
class ANTAS_NORTEAdmin(ImportExportModelAdmin):
    resource_class = ANTAS_NORTEResource
    list_display = ('VLAN', 'SERIAL', 'SERVICE_TAG', 'MODELO', 'NAME', 'IP', 'HOSTNAME', 'MAC', 'LOCAL', 'SWITCH_PORT', 'COMMENTS', 'DHCP',)
    search_fields = ('VLAN', 'SERIAL', 'SERVICE_TAG', 'MODELO', 'NAME', 'IP', 'HOSTNAME', 'MAC', 'LOCAL', 'SWITCH_PORT', 'COMMENTS', 'DHCP',)
    list_filter = ('VLAN', 'SERIAL', 'SERVICE_TAG', 'MODELO', 'NAME', 'IP', 'HOSTNAME', 'MAC', 'LOCAL', 'SWITCH_PORT', 'COMMENTS', 'DHCP',)
admin.site.register(ANTAS_NORTE, ANTAS_NORTEAdmin)

###########################################################################################################################################

class PANTERAResource(resources.ModelResource):
    class Meta:
        model = PANTERA
class PANTERAAdmin(ImportExportModelAdmin):
    resource_class = PANTERAResource
    list_display = ('VLAN', 'SERIAL', 'SERVICE_TAG', 'MODEL_HOST', 'TYPE', 'NAME', 'IP', 'HOSTNAME', 'MAC', 'LOCAL_COMMENT', 'SWITCH_PORT', 'DHCP_OPTION',)
    search_fields = ('VLAN', 'SERIAL', 'SERVICE_TAG', 'MODEL_HOST', 'TYPE', 'NAME', 'IP', 'HOSTNAME', 'MAC', 'LOCAL_COMMENT', 'SWITCH_PORT', 'DHCP_OPTION',)
    list_filter = ('VLAN', 'SERIAL', 'SERVICE_TAG', 'MODEL_HOST', 'TYPE', 'NAME', 'IP', 'HOSTNAME', 'MAC', 'LOCAL_COMMENT', 'SWITCH_PORT', 'DHCP_OPTION',)
admin.site.register(PANTERA, PANTERAAdmin)

###########################################################################################################################################

class PEDRABRANCAResource(resources.ModelResource):
    class Meta:
        model = PEDRABRANCA
class PEDRABRANCAAdmin(ImportExportModelAdmin):
    resource_class = PEDRABRANCAResource
    list_display = ('VLAN', 'SERIAL', 'SERVICE_TAG', 'NAME', 'IP', 'HOSTNAME', 'MAC', 'LOCAL', 'SWITCH_PORT',)
    search_fields = ('VLAN', 'SERIAL', 'SERVICE_TAG', 'NAME', 'IP', 'HOSTNAME', 'MAC', 'LOCAL', 'SWITCH_PORT',)
    list_filter = ('VLAN', 'SERIAL', 'SERVICE_TAG', 'NAME', 'IP', 'HOSTNAME', 'MAC', 'LOCAL', 'SWITCH_PORT',)
admin.site.register(PEDRABRANCA, PEDRABRANCAAdmin)

###########################################################################################################################################

class CANResource(resources.ModelResource):
    class Meta:
        model = CAN
class CANAdmin(ImportExportModelAdmin):
    resource_class = CANResource
    list_display = ('VLAN', 'SERIAL', 'SERVICE_TAG', 'MODEL_HOST', 'TYPE', 'NAME', 'IP', 'HOSTNAME', 'MAC', 'LOCAL_COMENT', 'SWITCH_PORT', 'DHCP_OPTION',)
    search_fields = ('VLAN', 'SERIAL', 'SERVICE_TAG', 'MODEL_HOST', 'TYPE', 'NAME', 'IP', 'HOSTNAME', 'MAC', 'LOCAL_COMENT', 'SWITCH_PORT', 'DHCP_OPTION',)
    list_filter = ('VLAN', 'SERIAL', 'SERVICE_TAG', 'MODEL_HOST', 'TYPE', 'NAME', 'IP', 'HOSTNAME', 'MAC', 'LOCAL_COMENT', 'SWITCH_PORT', 'DHCP_OPTION',)
admin.site.register(CAN, CANAdmin)

###########################################################################################################################################

class VLANsResource(resources.ModelResource):
    class Meta:
        model = VLANs
class VLANsAdmin(ImportExportModelAdmin):
    resource_class = VLANsResource
    list_display = ('VLAN', 'NAME', 'NAME_OBS', 'OUTROS', 'OUTROS_OBS',)
    search_fields = ('VLAN', 'NAME', 'NAME_OBS', 'OUTROS', 'OUTROS_OBS',)
    list_filter = ('VLAN', 'NAME', 'NAME_OBS', 'OUTROS', 'OUTROS_OBS',)
admin.site.register(VLANs, VLANsAdmin)

###########################################################################################################################################

class EXTERNAL_IPSResource(resources.ModelResource):
    class Meta:
        model = EXTERNAL_IPS
class EXTERNAL_IPSAdmin(ImportExportModelAdmin):
    resource_class = EXTERNAL_IPSResource
    list_display = ('Site', 'Provedor', 'Tipo', 'IP_01', 'Rota_2', 'IP_02', 'Gateway', 'Vlan',)
    search_fields = ('Site', 'Provedor', 'Tipo', 'IP_01', 'Rota_2', 'IP_02', 'Gateway', 'Vlan',)
    list_filter = ('Site', 'Provedor', 'Tipo', 'IP_01', 'Rota_2', 'IP_02', 'Gateway', 'Vlan',)
admin.site.register(EXTERNAL_IPS, EXTERNAL_IPSAdmin)

###########################################################################################################################################

class MATERIALResource(resources.ModelResource):
    class Meta:
        model = MATERIAL
class MATERIALAdmin(ImportExportModelAdmin):
    resource_class = MATERIALResource
    list_display = ('MATERIAL', 'VENDOR', 'QTD', 'MODELO', 'N_SERIE',)
    search_fields = ('MATERIAL', 'VENDOR', 'QTD', 'MODELO', 'N_SERIE',)
    list_filter = ('MATERIAL', 'VENDOR', 'QTD', 'MODELO', 'N_SERIE',)
admin.site.register(MATERIAL, MATERIALAdmin)

###########################################################################################################################################

# class CiscoResource(resources.ModelResource):
#     class Meta:
#         model = Cisco
# class CiscoAdmin(ImportExportModelAdmin):
#     resource_class = CiscoResource
#     list_display = ('hostname', 'vlan', 'ip', 'mac', 'nserie', 'fabricante', 'modelo', 'instaladoem', 'localidade', 'categoria', 'tipo', 'tipogestao', 'criado_em', 'atualizado_em', 'usuario', 'senha',)
#     search_fields = ('hostname', 'vlan', 'ip', 'mac', 'nserie', 'fabricante', 'modelo', 'instaladoem', 'localidade', 'categoria', 'tipo', 'tipogestao', 'criado_em', 'atualizado_em', 'usuario', 'senha',)
#     list_filter = ('hostname', 'vlan', 'ip', 'mac', 'nserie', 'fabricante', 'modelo', 'instaladoem', 'localidade', 'categoria', 'tipo', 'tipogestao', 'criado_em', 'atualizado_em', 'usuario', 'senha',)
# admin.site.register(Cisco, CiscoAdmin)

###########################################################################################################################################

# class intelbrasResource(resources.ModelResource):
#     class Meta:
#        model = intelbras
# class intelbrasAdmin(ImportExportModelAdmin):
#     resource_class = intelbrasResource
#     list_display = ('hostname', 'vlan', 'ip', 'mac', 'nserie', 'fabricante', 'modelo', 'instaladoem', 'localidade', 'categoria', 'tipo', 'tipogestao', 'criado_em', 'atualizado_em', 'usuario', 'senha',)
#     search_fields = ('hostname', 'vlan', 'ip', 'mac', 'nserie', 'fabricante', 'modelo', 'instaladoem', 'localidade', 'categoria', 'tipo', 'tipogestao', 'criado_em', 'atualizado_em', 'usuario', 'senha',)
#     list_filter = ('hostname', 'vlan', 'ip', 'mac', 'nserie', 'fabricante', 'modelo', 'instaladoem', 'localidade', 'categoria', 'tipo', 'tipogestao', 'criado_em', 'atualizado_em', 'usuario', 'senha',)
# admin.site.register(intelbras, intelbrasAdmin)

###########################################################################################################################################

class BHZResource(resources.ModelResource):
    class Meta:
        model = BHZ
class BHZAdmin(ImportExportModelAdmin):
    resource_class = BHZResource
    list_display = ('VLAN', 'SERIAL', 'SERVICE_TAG', 'MODEL_HOST', 'TYPE', 'NAME', 'IP', 'HOSTNAME', 'MAC', 'LOCAL_COMENT', 'SWITCH_PORT', 'DHCP_OPTION',)
    search_fields = ('VLAN', 'SERIAL', 'SERVICE_TAG', 'MODEL_HOST', 'TYPE', 'NAME', 'IP', 'HOSTNAME', 'MAC', 'LOCAL_COMENT', 'SWITCH_PORT', 'DHCP_OPTION',)
    list_filter = ('VLAN', 'SERIAL', 'SERVICE_TAG', 'MODEL_HOST', 'TYPE', 'NAME', 'IP', 'HOSTNAME', 'MAC', 'LOCAL_COMENT', 'SWITCH_PORT', 'DHCP_OPTION',)
admin.site.register(BHZ, BHZAdmin)

###########################################################################################################################################

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')

###########################################################################################################################################

# @admin.register(Celular)
# class Celular (admin.ModelAdmin): 
#    list_display = ('utilizador', 'matricula', 'status', 'departamento', 'email', 'datacompra', 'datarecebimento', 'telefone', 'imeidochip', 'operadora', 'fabricante', 'modelo', 'memoriaram', 'armazenamento', 'numerodeserie',)
#    search_fields = ('utilizador', 'matricula', 'status', 'departamento', 'email', 'datacompra', 'datarecebimento', 'telefone', 'imeidochip', 'operadora', 'fabricante', 'modelo', 'memoriaram', 'armazenamento', 'numerodeserie',)
#    list_filter = ('utilizador', 'matricula', 'status', 'departamento', 'email', 'datacompra', 'datarecebimento', 'telefone', 'imeidochip', 'operadora', 'fabricante', 'modelo', 'memoriaram', 'armazenamento', 'numerodeserie',)

###########################################################################################################################################

# @admin.register(Rede)
# class Rede (admin.ModelAdmin): 
#    list_display = ('utilizador', 'matricula', 'departamento', 'email', 'datacompra', 'datarecebimento', 'telefone', 'imeidochip', 'fabricante', 'modelo', 'memoriaram', 'armazenamento', 'numerodeserie',)
#    search_fields = ('utilizador', 'matricula', 'departamento', 'email', 'datacompra', 'datarecebimento', 'telefone', 'imeidochip', 'fabricante', 'modelo', 'memoriaram', 'armazenamento', 'numerodeserie',)

###########################################################################################################################################

# @admin.register(Radio)
# class Radio (admin.ModelAdmin): 
#    list_display = ('utilizador', 'matricula', 'departamento', 'email', 'datacompra', 'datarecebimento', 'telefone', 'imeidochip', 'fabricante', 'modelo', 'memoriaram', 'armazenamento', 'numerodeserie',)
#    search_fields = ('utilizador', 'matricula', 'departamento', 'email', 'datacompra', 'datarecebimento', 'telefone', 'imeidochip', 'fabricante', 'modelo', 'memoriaram', 'armazenamento', 'numerodeserie',)

###########################################################################################################################################
