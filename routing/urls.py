from django.urls import path
from routing import views

app_name = 'routing'

urlpatterns = [
    path('', views.RoutingListView.as_view(), name='routing_list'),
    path('create/', views.create_routing, name='routing_create'),
    path('delete/<int:pk>/', views.RoutingDeleteView.as_view(), name='routing_delete'),
    path('reload_instance/', views.reload_instance, name='reload_instance'),
]