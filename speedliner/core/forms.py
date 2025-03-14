from django import forms
from .models import Customer, Booking, Vehicle, Payment

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'contact_info', 'location']

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['name', 'number_plate', 'capacity', 'available']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer', 'vehicle', 'service_date', 'return_date']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['booking', 'amount']
