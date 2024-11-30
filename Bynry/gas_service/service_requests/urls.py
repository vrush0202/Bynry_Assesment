# gas_service/apps/service_requests/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_request_list, name='service_request_list'),  # Default page for service requests
    path('create/', views.service_request_create, name='service_request_create'),  # Service request creation
    path('<int:id>/', views.service_request_detail, name='service_request_detail'),  # Detail of a specific request
]
