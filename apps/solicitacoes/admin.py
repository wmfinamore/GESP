from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Servico, Solicitacao


class ServicosHistoryAdmin(SimpleHistoryAdmin):
    pass


class SolicitacaoHistoryAdmin(SimpleHistoryAdmin):
    pass


admin.site.register(Servico, ServicosHistoryAdmin)
admin.site.register(Solicitacao, SolicitacaoHistoryAdmin)
