from django.urls import path
from client import views

app_name = 'routing'

urlpatterns = [
    path('', views.ClientListView.as_view(), name='routing_list'),
    path('create/', views.ClientCreateView.as_view(), name='routing_create'),
    path('edit/<int:pk>/', views.ClientUpdateView.as_view(), name='routing_edit'),
    path('delete/<int:pk>/', views.ClientDeleteView.as_view(), name='routing_delete'),
]
