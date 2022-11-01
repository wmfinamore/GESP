from django.db import models
from apps.core.models import Auditoria
from apps.solicitacoes.models import Solicitacao
from django.db.models.signals import post_save
from django.dispatch import receiver


STATUS_SERVICO = [
    ('em_andamento', 'Em Andamento'),
    ('resolvido', 'Resolvido'),
    ('respondido', 'Respondido'),
]


class OrdemServico(Auditoria):
    solicitacoes = models.ManyToManyField(Solicitacao, blank=True, related_name='ordem_servico',
                                          verbose_name='Solicitações', limit_choices_to={'numero_ordem': None})
    detalhe_servico = models.TextField(null=True, blank=True, verbose_name='Detalhes do Serviço')
    data_execucao = models.DateField(null=True, blank=True, verbose_name='Data de Execução')
    status_servico = models.CharField(max_length=15, null=True, blank=True, choices=STATUS_SERVICO,
                                      verbose_name='Status do Serviço')
    observacao = models.TextField(null=True, blank=True, verbose_name='Observações')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordens de Serviço'
        ordering = ['-data_inclusao']


@receiver(post_save, sender=OrdemServico)
def update_solicitacao(sender, instance, **kwargs):
    instance.solicitacoes.all().update(numero_ordem=instance.id)
