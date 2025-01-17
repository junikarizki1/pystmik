from django.shortcuts import render
from .models import Writer

def index(request):
    penulis = Writer.objects.all()
    context={
        'Title':'Penulis',
        'Heading':'Daftar Penulis',
        'Penulis':penulis,
    }
    return render(request,'penulis.html',context)
