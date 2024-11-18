from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Customer, ServiceRequest
from .forms import ServiceRequestForm, UserRegistrationForm
from django.db import transaction
from django.utils import timezone

@transaction.atomic
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = form.save()
                    login(request, user)
                    messages.success(request, 'Registration successful! Welcome to Gas Utility Portal.')
                    return redirect('customer_portal:home')
            except Exception as e:
                messages.error(request, 'An error occurred during registration. Please try again.')
                return redirect('customer_portal:register')
    else:
        form = UserRegistrationForm()
    return render(request, 'customer_portal/register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'customer_portal/home.html')

@login_required
def service_request_create(request):
    try:
        customer = request.user.customer
    except Customer.DoesNotExist:
        # Create a new customer profile if it doesn't exist
        customer = Customer.objects.create(
            user=request.user,
            phone_number='',
            address='',
        )
        messages.warning(request, 'Please update your profile information.')
    
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = customer
            service_request.save()
            messages.success(request, 'Service request submitted successfully!')
            return redirect('customer_portal:service_request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_portal/service_request_form.html', {'form': form})

@login_required
def service_request_list(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'customer_portal/service_request_list.html', {
        'service_requests': service_requests
    })

@login_required
def service_request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk, customer=request.user.customer)
    return render(request, 'customer_portal/service_request_detail.html', {
        'service_request': service_request
    })