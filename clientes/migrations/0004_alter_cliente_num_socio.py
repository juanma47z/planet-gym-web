# Generated by Django 4.2 on 2024-10-02 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_cliente_num_socio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='num_socio',
            field=models.IntegerField(),
        ),
    ]
