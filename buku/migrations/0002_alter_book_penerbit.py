# Generated by Django 5.1.2 on 2024-12-13 07:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buku', '0001_initial'),
        ('penerbit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='penerbit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='penerbit.publisher'),
        ),
    ]
