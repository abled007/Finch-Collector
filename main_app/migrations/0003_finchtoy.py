# Generated by Django 4.0.4 on 2022-04-30 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_finch_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinchToy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
            ],
        ),
    ]
