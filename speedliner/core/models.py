from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="bookings")
    service_date = models.DateField()
    destination = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.customer.name} on {self.service_date}"


class Vehicle(models.Model):
    name = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} for {self.booking}"
