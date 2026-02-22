from django.urls import path
from . import views

urlpatterns = [
    path('', views.evidence_list, name='evidence_list'),
    path('add/', views.evidence_add, name='evidence_add'),
    path('<int:evidence_id>/', views.evidence_detail, name='evidence_detail'),
    path('<int:evidence_id>/delete/', views.evidence_delete, name='evidence_delete'),
]