from django.contrib import admin
from .models import Customer, ServiceRequest, CustomerSupport

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'user', 'phone_number')
    search_fields = ('customer_id', 'user__username', 'phone_number')
    list_filter = ('user__date_joined',)

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer', 'request_type', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'request_type', 'created_at')
    search_fields = ('customer__customer_id', 'description')
    date_hierarchy = 'created_at'

@admin.register(CustomerSupport)
class CustomerSupportAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'user', 'department')
    search_fields = ('employee_id', 'user__username', 'department')