from django.db import models
from penerbit.models import Publisher

class Book(models.Model):
    kode_buku=models.CharField(max_length=4)
    judul_buku=models.CharField(max_length=100)
    pengarang=models.CharField(max_length=50)
    penerbit= models.ForeignKey(Publisher, on_delete=models.CASCADE, default=1) 
    tahun=models.CharField(max_length=4)

    def __str__(self):
        return self.judul_buku
# penerbit agak beda supaya terintegrasi, biar pas  input di buku, penerbitnya langsung bisa dipilih