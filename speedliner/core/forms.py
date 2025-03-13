from django import forms
from .models import Customer, Booking, Vehicle, Payment

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'contact_info', 'location']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer', 'service_date', 'destination']

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['name', 'capacity', 'available']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['booking', 'amount']
