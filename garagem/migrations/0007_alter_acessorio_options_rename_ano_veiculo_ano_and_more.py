# Generated by Django 4.1.7 on 2023-03-31 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0006_alter_cor_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acessorio',
            options={'verbose_name': 'acessório', 'verbose_name_plural': 'acessórios'},
        ),
        migrations.RenameField(
            model_name='veiculo',
            old_name='Ano',
            new_name='ano',
        ),
        migrations.RenameField(
            model_name='veiculo',
            old_name='Modelo',
            new_name='modelo',
        ),
        migrations.RenameField(
            model_name='veiculo',
            old_name='Preco',
            new_name='preco',
        ),
    ]
