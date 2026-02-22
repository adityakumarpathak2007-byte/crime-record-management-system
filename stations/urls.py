from django.urls import path
from . import views

urlpatterns = [
    path('', views.station_list, name='station_list'),
    path('add/', views.station_add, name='station_add'),
    path('<int:station_id>/', views.station_detail, name='station_detail'),
    path('<int:station_id>/delete/', views.station_delete, name='station_delete'),
]