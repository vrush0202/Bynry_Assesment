# gas_service/apps/service_requests/views.py
from django.shortcuts import render

# Example view for listing service requests
def service_request_list(request):
    return render(request, 'service_requests/list.html')

# Example view for creating a service request
def service_request_create(request):
    return render(request, 'service_requests/create.html')

# Example view for viewing a specific service request
def service_request_detail(request, id):
    return render(request, 'service_requests/detail.html')
