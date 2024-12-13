from django.shortcuts import render
from .models import Publisher

def index(request):
    penerbit = Publisher.objects.all()
    context={
        'Title':'Penerbit',
        'Heading':'Daftar Penerbit',
        'Penerbit':penerbit,
    }
    return render(request,'penerbit.html',context)
