# Generated by Django 4.2.4 on 2023-08-25 13:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0002_veiculo_fotos"),
    ]

    operations = [
        migrations.AddField(
            model_name="veiculo",
            name="acessorio",
            field=models.ManyToManyField(
                related_name="veiculo", to="garagem.acessorio"
            ),
        ),
    ]
