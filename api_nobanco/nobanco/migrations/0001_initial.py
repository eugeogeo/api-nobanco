# Generated by Django 4.1.7 on 2023-03-22 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cpf', models.CharField(max_length=14)),
                ('email', models.CharField(max_length=100)),
                ('celular', models.CharField(max_length=15)),
                ('nome', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=80)),
            ],
        ),
    ]
