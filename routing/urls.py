from django.urls import path

from .views import RouteListView, AddRoutingView, ReloadInstance

app_name = 'routing'

urlpatterns = [
    path('list-routes/', RouteListView.as_view(), name="RouteListView"),
    path('add-routing/', AddRoutingView.as_view(), name="AddRoutingView"),
    path('reload-instance/', ReloadInstance.as_view(), name="ReloadInstance")
]