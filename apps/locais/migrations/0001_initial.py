# Generated by Django 4.1.2 on 2022-10-30 01:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inclusao', models.DateField(auto_now_add=True, verbose_name='Data de Inclusão')),
                ('hora_inclusao', models.TimeField(auto_now_add=True, verbose_name='Hora de Inclusão')),
                ('data_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data de Alteração')),
                ('hora_alteracao', models.TimeField(auto_now=True, verbose_name='Hora de Alteração')),
                ('logradouro', models.CharField(blank=True, max_length=150, null=True, verbose_name='Logradouro')),
                ('bairro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bairro')),
                ('cep', models.CharField(blank=True, max_length=8, null=True, verbose_name='CEP')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
                'ordering': ['logradouro', 'bairro'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalEndereco',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('data_inclusao', models.DateField(blank=True, editable=False, verbose_name='Data de Inclusão')),
                ('hora_inclusao', models.TimeField(blank=True, editable=False, verbose_name='Hora de Inclusão')),
                ('data_alteracao', models.DateTimeField(blank=True, editable=False, verbose_name='Data de Alteração')),
                ('hora_alteracao', models.TimeField(blank=True, editable=False, verbose_name='Hora de Alteração')),
                ('logradouro', models.CharField(blank=True, max_length=150, null=True, verbose_name='Logradouro')),
                ('bairro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bairro')),
                ('cep', models.CharField(blank=True, max_length=8, null=True, verbose_name='CEP')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Endereço',
                'verbose_name_plural': 'historical Endereços',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
