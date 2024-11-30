# gas_service/gas_service/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('service_requests/', include('service_requests.urls')),  # Include the app URLs
    path('accounts/', include('accounts.urls')),  # Include the accounts URLs
]
