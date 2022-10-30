# Generated by Django 4.1.2 on 2022-10-30 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacoes', '0002_rename_historicalservicos_historicalservico_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalservico',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Serviço', 'verbose_name_plural': 'historical Serviços'},
        ),
        migrations.AlterModelOptions(
            name='servico',
            options={'ordering': ['nome'], 'verbose_name': 'Serviço', 'verbose_name_plural': 'Serviços'},
        ),
    ]
