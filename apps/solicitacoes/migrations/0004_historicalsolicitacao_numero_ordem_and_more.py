# Generated by Django 4.1.2 on 2022-11-01 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacoes', '0003_alter_historicalservico_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalsolicitacao',
            name='numero_ordem',
            field=models.PositiveBigIntegerField(blank=True, editable=False, null=True, verbose_name='Número da O.S.'),
        ),
        migrations.AddField(
            model_name='solicitacao',
            name='numero_ordem',
            field=models.PositiveBigIntegerField(blank=True, editable=False, null=True, verbose_name='Número da O.S.'),
        ),
    ]