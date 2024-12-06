from django.db import models

class Member(models.Model):
    kode_anggota=models.CharField(max_length=4)
    nama_anggota=models.CharField(max_length=100)
    jenis_kelamin=models.CharField(max_length=50)
    telepon=models.CharField(max_length=40)
    angkatan=models.CharField(max_length=4)
    alamat=models.CharField(max_length=250)

    def __str__(self):
        return self.nama_anggota
