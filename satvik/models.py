from django.db import models
from django.contrib.auth.models import User

# Model goes here 

class Table(models.Model):
    table_number = models.IntegerField(unique=True)  # Corresponds to HTML number input
    capacity = models.IntegerField(unique=True)  # Corresponds to HTML number input
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return f'Table {self.table_number} - Capacity: {self.capacity}'


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Corresponds to HTML select dropdown
    table = models.ForeignKey(Table, on_delete=models.CASCADE)  # Corresponds to HTML select dropdown
    date = models.DateField(auto_now_add=True)  # Corresponds to HTML date input
    time = models.TimeField(auto_now_add=True)  # Corresponds to HTML time input
    guest_count = models.IntegerField(default=1) 
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Reservation for {self.user.username} on {self.date} at {self.time}'