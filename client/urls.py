from django.urls import path
from client import views

app_name = 'client'

urlpatterns = [
    path('', views.ClientListView.as_view(), name='client_list'),
    path('create/', views.ClientCreateView.as_view(), name='client_create'),
    path('edit/<int:pk>/', views.ClientUpdateView.as_view(), name='client_edit'),
    path('delete/<int:pk>/', views.ClientDeleteView.as_view(), name='client_delete'),
]
