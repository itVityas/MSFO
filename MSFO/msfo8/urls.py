from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_msfo8'),
    path('upload_files/', views.upload_files, name='upload_files'),
    path('success/<int:id>/', views.success, name='success'),
    path('download/<int:id>/', views.download_file, name='download_file'),
    path('delete_all_reports/', views.delete_all_reports, name='delete_all_reports'),
    path('files_list/', views.files_list, name='files_list'),
    path('file_detail/<int:id>/', views.file_detail, name='file_detail'),
    path('success/', views.success, name='success'),
]
