# Generated by Django 5.0.3 on 2024-03-07 11:06

import core.models
import django.db.models.deletion
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateField(auto_now=True, verbose_name='modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('cargo', models.CharField(max_length=50, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Portifolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateField(auto_now=True, verbose_name='modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('cabecalio', models.CharField(max_length=50, verbose_name='Cabeçalio')),
                ('sublinha', models.CharField(max_length=30, verbose_name='Sublinha')),
                ('sobre', models.CharField(max_length=100, verbose_name='Sobre')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 450, 'width': 600}}, verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Portifolio',
                'verbose_name_plural': 'Portifolios',
            },
        ),
        migrations.CreateModel(
            name='Sobre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateField(auto_now=True, verbose_name='modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('data', models.CharField(max_length=50, verbose_name='Data')),
                ('cabecalio', models.CharField(max_length=50, verbose_name='Cabeçalio')),
                ('sobre', models.CharField(max_length=100, verbose_name='Sobre')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 200, 'width': 200}}, verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Sobre',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateField(auto_now=True, verbose_name='modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 500, 'width': 500}}, verbose_name='Imagem')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('x', models.CharField(default='#', max_length=100, verbose_name='x')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cargo', verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Funcionario',
                'verbose_name_plural': 'Funcionarios',
            },
        ),
    ]
