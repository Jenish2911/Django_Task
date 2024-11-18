from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', 
         auth_views.LoginView.as_view(
             template_name='customer_portal/login.html',
             next_page='customer_portal:home'
         ), 
         name='login'),
    path('accounts/logout/', 
         auth_views.LogoutView.as_view(
             next_page='login'
         ), 
         name='logout'),
    path('accounts/password_change/', 
         auth_views.PasswordChangeView.as_view(
             template_name='customer_portal/password_change.html',
             success_url='/accounts/password_change/done/',
         ),
         name='password_change'),
    path('accounts/password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='customer_portal/password_change_done.html'
         ),
         name='password_change_done'),
    path('', include('customer_portal.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)