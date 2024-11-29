from django.db import models

class Book(models.Model):
    kode_buku=models.CharField(max_length=4)
    judul_buku=models.CharField(max_length=100)
    pengarang=models.CharField(max_length=50)
    penerbit=models.CharField(max_length=40)
    tahun=models.CharField(max_length=4)

    def __str__(self):
        return self.judul_buku
