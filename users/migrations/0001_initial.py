# Generated by Django 4.1.7 on 2023-04-03 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('accountType', models.BooleanField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cellPhone', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('date', models.DateTimeField()),
                ('place', models.CharField(max_length=100)),
                ('balanceId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.balance')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('accountType', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
        migrations.AddField(
            model_name='balance',
            name='accountId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.generalaccount'),
        ),
    ]
