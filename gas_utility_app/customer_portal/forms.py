from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer, ServiceRequest

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 
                 'password1', 'password2', 'phone_number', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
            # Create the associated Customer profile
            Customer.objects.create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                address=self.cleaned_data['address']
            )
        return user

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description', 'attachment']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'request_type': forms.Select(attrs={'class': 'form-control'}),
            'attachment': forms.FileInput(attrs={'class': 'form-control'})
        }