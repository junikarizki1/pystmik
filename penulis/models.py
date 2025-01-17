from django.db import models

class Writer(models.Model):
    kode_penulis=models.CharField(max_length=4)
    nama_penulis=models.CharField(max_length=100)
    alamat_penulis=models.CharField(max_length=200)
    kota_penulis=models.CharField(max_length=50)
    kontak_penulis=models.CharField(max_length=12)
    email_penulis=models.CharField(max_length=50)

    def __str__(self):
        return self.nama_penulis
