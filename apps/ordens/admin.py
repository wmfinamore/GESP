from django.contrib import admin
from .models import OrdemServico
from simple_history.admin import SimpleHistoryAdmin


class OrdemServicoHistoryAdmin(SimpleHistoryAdmin):
    filter_horizontal = ('solicitacoes', )
    list_display = ['id', 'status_servico', 'data_execucao', 'detalhe_servico', ]
    search_fields = ['id', 'observacao', 'detalhe_servico', ]
    list_filter = ['status_servico', 'data_execucao', ]
    fieldsets = (
        (None, {
            'fields': (
                ('solicitacoes', ),
                ('detalhe_servico',),
                ('status_servico', 'data_execucao', ),
                ('observacao', ),
            )
        }),
    )


admin.site.register(OrdemServico, OrdemServicoHistoryAdmin)
