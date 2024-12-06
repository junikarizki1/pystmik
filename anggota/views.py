from django.shortcuts import render
from .models import Member

def index(request):
    anggota = Member.objects.all()
    context={
        'Title':'Anggota Perpustakaan STMIK Pontianak',
        'Heading':'Daftar Anggota',
        'Anggota':anggota,
    }
    return render(request,'anggota.html',context)
