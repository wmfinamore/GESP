from django.contrib import admin
from .models import OrdemServico
from simple_history.admin import SimpleHistoryAdmin


class OrdemServicoHistoryAdmin(SimpleHistoryAdmin):
    filter_horizontal = ('solicitacoes', )


admin.site.register(OrdemServico, OrdemServicoHistoryAdmin)
