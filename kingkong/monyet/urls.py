from django.contrib import admin 
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings 

# import View dari todo Application
from .views import index_view, say_view, create_view, update_view, delete_view

app_name = 'monyet'
urlpatterns = [
    # url untuk halaman daftar task
    path('', index_view, name='index'),
    # url untuk halaman detail task
    path('<int:task_id>', say_view, name='say'),
    # url untuk halaman tambah task
    path('create', create_view, name='create'),
    # url untuk halaman ubah task
    path('update/<int:task_id>', update_view, name='update'),
    # url untuk menghapus task
    path('delete/<int:task_id>', delete_view, name='delete'),
]