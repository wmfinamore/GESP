from django.contrib import admin
from .models import Endereco
from simple_history.admin import SimpleHistoryAdmin


class EnderecoHistoryAdmin(SimpleHistoryAdmin):
    search_fields = ['logradouro', 'bairro', 'cep', ]
    list_display = ['logradouro', 'bairro', 'cep', ]


admin.site.register(Endereco, EnderecoHistoryAdmin)
