from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home_msfo8'),
    path('upload_files/', views.upload_files, name='upload_files'),
    path('success/<int:id>/', views.success, name='success'),
    path('download/<int:id>/', views.download_file, name='download_file'),
    path('delete_all_reports/', views.delete_all_reports, name='delete_all_reports'),
    path('files_list/', views.files_list, name='files_list'),
    path('file_detail/<int:id>', views.file_detail, name='file_detail')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
