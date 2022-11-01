from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Servico, Solicitacao


class ServicosHistoryAdmin(SimpleHistoryAdmin):
    list_display = ['nome', 'status', ]
    search_fields = ['nome', ]
    list_filter = ['status', ]


class SolicitacaoHistoryAdmin(SimpleHistoryAdmin):
    list_display = ['tipo_origem', 'numero_documento', 'endereco', 'numero_endereco', 'tipo_servico',
                    'numero_ordem', ]
    search_fields = ['numero_documento', 'endereco__logradouro', 'endereco__bairro', 'endereco__bairro', ]
    list_filter = ['data_entrada', 'tipo_servico']
    fieldsets = (
        (None, {
            'fields': (
                ('tipo_servico', 'natureza_solicitante', 'prazo_resposta', ),
                ('tipo_origem', 'numero_documento', 'data_entrada'),
            )
        }),
        ('Detalhes da Solicitação', {
            'fields': (
                ('endereco', 'numero_endereco',),
                ('informacao_extra_local',),

            )
        }),
    )
    autocomplete_fields = ['endereco', ]


admin.site.register(Servico, ServicosHistoryAdmin)
admin.site.register(Solicitacao, SolicitacaoHistoryAdmin)
