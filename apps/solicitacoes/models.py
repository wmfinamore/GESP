from django.db import models
from apps.core.models import Auditoria
from apps.locais.models import Endereco
from datetime import date


class Servicos(Auditoria):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome',]


TIPOS_ORIGEM = [
    ('156', '156'),
    ('oficio', 'Ofício'),
    ('indicacao', 'Indicação'),
]


NATUREZA_SOLICITANTE = [
    ('municipe', 'Munícipe'),
    ('vereador', 'Vereador'),
    ('outros', 'Outros'),
]


class Solicitacao(Auditoria):
    tipo_origem = models.CharField(max_length=15, null=True, blank=True, choices=TIPOS_ORIGEM,
                                   verbose_name='Tipos de Origem')
    numero_documento = models.CharField(max_length=25, null=True, blank=True, verbose_name='Número do Documento')
    data_entrada = models.DateField(verbose_name='Data de Entrada', null=True, blank=True)
    tipo_servico = models.ForeignKey(Servicos, on_delete=models.PROTECT, null=True, blank=True,
                                     verbose_name='Tipo de servico', limit_choices_to={'status': True})
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Endereço')
    numero_endereco = models.CharField(max_length=6, null=True, blank=True, verbose_name='Número do Endereço')
    informacao_extra_local = models.TextField(null=True, blank=True, verbose_name='Informação Extra do Local')
    natureza_solicitante = models.CharField(max_length=15, null=True, blank=True, choices=NATUREZA_SOLICITANTE,
                                            verbose_name='Natureza do Solicitante')
    prazo_resposta = models.DateField(verbose_name='Prazo para resposta', null=True, blank=True)

    def __str__(self):
        return str(self.tipo_origem) + ' - ' + str(self.numero_documento) + ' - ' \
               + str(self.endereco) + ' - ' + str(self.tipo_servico)


    class Meta:
        verbose_name = 'Solicitação'
        verbose_name_plural = 'Solicitações'
        ordering = ['-data_entrada', 'endereco__logradouro']
