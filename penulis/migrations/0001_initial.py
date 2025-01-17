# Generated by Django 5.1.2 on 2024-12-20 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_penulis', models.CharField(max_length=4)),
                ('nama_penulis', models.CharField(max_length=100)),
                ('alamat_penulis', models.CharField(max_length=200)),
                ('kota_penulis', models.CharField(max_length=50)),
                ('kontak_penulis', models.CharField(max_length=12)),
                ('email_penulis', models.CharField(max_length=50)),
            ],
        ),
    ]
