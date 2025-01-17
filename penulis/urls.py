from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name='penulis'),
]
# name boleh ada atau ndk juga gpp, fungsinya buat manggil di index file nanti biar bisa bolak balek menu