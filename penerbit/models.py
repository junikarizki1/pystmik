from django.db import models

class Publisher(models.Model):
    kode_penerbit=models.CharField(max_length=4)
    nama_penerbit=models.CharField(max_length=100)
    alamat_penerbit=models.CharField(max_length=200)
    kota_penerbit=models.CharField(max_length=50)
    kontak_penerbit=models.CharField(max_length=12)
    email_penerbit=models.CharField(max_length=50)

    def __str__(self):
        return self.nama_penerbit
