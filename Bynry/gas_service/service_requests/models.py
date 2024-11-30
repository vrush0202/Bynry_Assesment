from django.db import models


from django.db import models

class ServiceRequest(models.Model):
    SERVICE_CHOICES = [
        ('Installation', 'Installation'),
        ('Repair', 'Repair'),
        ('Complaint', 'Complaint'),
    ]

    customer_name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    description = models.TextField()
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.customer_name} - {self.service_type} - {self.status}'
