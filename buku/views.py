from django.shortcuts import render
from .models import Book

def index(request):
    buku = Book.objects.all()
    context={
        'Title':'Perpustakaan STMIK Pontianak',
        'Heading':'Daftar Buku Ilmu Komputer',
        'Buku':buku,
    }
    return render(request,'index.html',context)