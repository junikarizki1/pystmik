from django.shortcuts import render, redirect
from .models import Book
from django.http import HttpResponse
from penerbit.models import Publisher

def index(request):
    buku = Book.objects.all()
    context={
        'Title':'Perpustakaan STMIK Pontianak',
        'Heading':'Daftar Buku Ilmu Komputer',
        'Buku':buku,
    }
    return render(request,'buku.html',context)

def bukuadd(request):
    penerbit_list = Publisher.objects.all()
    context={
        'Title':'Perpustakaan STMIK Pontianak',
        'Heading':'Form Pengisian Data Buku',
        'penerbit_list': penerbit_list,
    }
    return render(request,'bukuadd.html',context)

def process_bukuadd(request):
    
    if request.method == 'POST':
        kode_buku = request.POST.get('kode_buku')
        judul_buku = request.POST.get('judul_buku')
        pengarang = request.POST.get('pengarang')
        penerbit_id = request.POST.get('penerbit')
        tahun = request.POST.get('tahun')

        try:
            penerbit = Publisher.objects.get(id=penerbit_id)
        except Publisher.DoesNotExist:
            return HttpResponse('Penerbit tidak ditemukan.')

        buku = Book(kode_buku=kode_buku, judul_buku=judul_buku, pengarang=pengarang, penerbit=penerbit, tahun=tahun)
        buku.save()
        return redirect('../../buku')
    else:
        return HttpResponse('Invalid request method.') 