# Generated by Django 4.1.7 on 2023-04-02 19:38

from django.db import migrations, models
import usuarios.models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='senha',
            field=models.CharField(max_length=80, validators=[usuarios.models.validate_senha]),
        ),
    ]