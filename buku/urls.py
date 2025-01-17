from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name='buku'),
    path('bukuadd/', views.bukuadd, name='bukuadd'),
    path('process_bukuadd/', views.process_bukuadd, name='process_bukuadd'),
]