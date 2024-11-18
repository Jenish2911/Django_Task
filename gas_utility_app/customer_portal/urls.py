from django.urls import path
from . import views

app_name = 'customer_portal'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('service-requests/create/', views.service_request_create, name='service_request_create'),
    path('service-requests/', views.service_request_list, name='service_request_list'),
    path('service-requests/<int:pk>/', views.service_request_detail, name='service_request_detail'),
]