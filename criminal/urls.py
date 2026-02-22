from django.urls import path
from . import views

urlpatterns = [
    path('', views.criminal_list, name='criminal_list'),
    path('add/', views.criminal_add, name='criminal_add'),
    path('<int:criminal_id>/', views.criminal_detail, name='criminal_detail'),
    path('<int:criminal_id>/delete/', views.criminal_delete, name='criminal_delete'),
]