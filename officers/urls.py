from django.urls import path
from . import views

urlpatterns = [
    path('', views.officer_list, name='officer_list'),
    path('add/', views.officer_add, name='officer_add'),
    path('<int:officer_id>/', views.officer_detail, name='officer_detail'),
    path('<int:officer_id>/delete/', views.officer_delete, name='officer_delete'),
]