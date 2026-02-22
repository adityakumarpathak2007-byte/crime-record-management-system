from django.urls import path
from . import views

urlpatterns = [
    path('', views.court_list, name='court_list'),
    path('add/', views.court_add, name='court_add'),
    path('<int:court_id>/', views.court_detail, name='court_detail'),
    path('<int:court_id>/delete/', views.court_delete, name='court_delete'),
]