# Generated by Django 4.1.2 on 2022-10-30 02:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('solicitacoes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HistoricalServicos',
            new_name='HistoricalServico',
        ),
        migrations.RenameModel(
            old_name='Servicos',
            new_name='Servico',
        ),
        migrations.AlterModelOptions(
            name='historicalservico',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical servico', 'verbose_name_plural': 'historical servicos'},
        ),
    ]
