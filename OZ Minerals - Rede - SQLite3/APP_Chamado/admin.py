from django.contrib import admin
from .models import Chamado

class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'tipodechamado', 'status', 'criado_em', 'atualizado_em', 'usuario')
    search_fields = ('ticket', 'tipodechamado', 'descricao', 'usuario__username')
    list_filter = ('status', 'criado_em', 'atualizado_em', 'usuario')
    readonly_fields = ('ticket',)

admin.site.register(Chamado, ChamadoAdmin)