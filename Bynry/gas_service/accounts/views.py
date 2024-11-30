# gas_service/apps/accounts/views.py
from django.shortcuts import render

# Example login view
def login_view(request):
    return render(request, 'accounts/login.html')

# Example register view
def register_view(request):
    return render(request, 'accounts/register.html')
