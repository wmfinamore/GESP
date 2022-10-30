from django.db import models
from apps.core.models import Auditoria


class Endereco(Auditoria):
    logradouro = models.CharField(max_length=150, null=True, blank=True, verbose_name='Logradouro')
    bairro = models.CharField(max_length=50, null=True, blank=True, verbose_name='Bairro')
    cep = models.CharField(max_length=8, null=True, blank=True, verbose_name='CEP')

    def __str__(self):
        return str(self.logradouro) + ', ' + str(self.bairro)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        ordering = ['logradouro', 'bairro']
