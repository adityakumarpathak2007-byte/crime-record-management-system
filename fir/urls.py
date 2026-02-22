from django.urls import path
from . import views

urlpatterns = [
    path('', views.fir_list, name='fir_list'),
    path('register/', views.fir_register, name='fir_register'),
    path('<int:fir_id>/', views.fir_detail, name='fir_detail'),
    path('<int:fir_id>/update-status/', views.fir_update_status, name='fir_update_status'),
    path('<int:fir_id>/delete/', views.fir_delete, name='fir_delete'),
]