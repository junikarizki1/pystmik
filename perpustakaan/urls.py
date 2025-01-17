from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('buku/',include('buku.urls')),
    path('anggota/',include('anggota.urls')),
    path('penerbit/',include('penerbit.urls')),
    path('penulis/',include('penulis.urls')),
]
