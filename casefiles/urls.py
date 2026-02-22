from django.urls import path
from . import views

urlpatterns = [
    path('', views.case_list, name='case_list'),
    path('add/', views.case_add, name='case_add'),
    path('<int:case_id>/', views.case_detail, name='case_detail'),
    path('<int:case_id>/update-status/', views.case_update_status, name='case_update_status'),
    path('<int:case_id>/delete/', views.case_delete, name='case_delete'),
]