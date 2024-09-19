# satvik/forms.py

from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'time', 'guest_count', 'special_request']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'guest_count': forms.NumberInput(attrs={'min': 1}),
            'special_request': forms.Textarea(attrs={'rows': 4}),
        }
