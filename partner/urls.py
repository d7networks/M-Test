from django.urls import path
from partner import views

app_name = 'partner'

urlpatterns = [
    path('', views.PartnerListView.as_view(), name='partner_list'),
    path('create/', views.PartnerCreateView.as_view(), name='partner_create'),
    path('edit/<int:pk>/', views.PartnerUpdateView.as_view(), name='partner_edit'),
    path('delete/<int:pk>/', views.PartnerDeleteView.as_view(), name='partner_delete'),
]
