from django.utils import timezone
import random
import string
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    customer_id = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def generate_unique_customer_id():
        """Generate a unique customer ID."""
        while True:
            # Get current year's last two digits
            year = str(timezone.now().year)[2:]
            # Generate random components
            letters = ''.join(random.choices(string.ascii_uppercase, k=2))
            numbers = ''.join(random.choices(string.digits, k=4))
            # Combine into customer ID
            customer_id = f"CUST{year}{letters}{numbers}"
            # Check if this ID already exists
            if not Customer.objects.filter(customer_id=customer_id).exists():
                return customer_id

    def save(self, *args, **kwargs):
        if not self.customer_id:
            self.customer_id = self.generate_unique_customer_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer_id} - {self.user.get_full_name()}"

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
        ('CLOSED', 'Closed'),
    ]
    
    REQUEST_TYPES = [
        ('GAS_LEAK', 'Gas Leak'),
        ('CONNECTION', 'New Connection'),
        ('BILLING', 'Billing Issue'),
        ('MAINTENANCE', 'Maintenance'),
        ('OTHER', 'Other'),
    ]
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    description = models.TextField()
    attachment = models.FileField(upload_to='service_requests/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.customer.customer_id} - {self.request_type} - {self.status}"

    class Meta:
        ordering = ['-created_at']

class CustomerSupport(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.employee_id}"