from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('upload_files', views.upload_files, name='upload_files'),
    path('success/<int:id>', views.success, name='success'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
