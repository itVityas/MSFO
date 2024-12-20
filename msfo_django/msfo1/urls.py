from django.urls import path
from . import views

urlpatterns = [
    path('', views.msfo1_home, name='msfo1_home'),
    path('generate_report/', views.msfo1_generate_report_view, name='msfo1_generate_report'),
    path('reports/', views.msfo1_report_list, name='msfo1_report_list'),
    path('reports/<int:pk>/', views.msfo1_report_detail, name='msfo1_report_detail')
]
