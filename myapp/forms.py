# forms.py

from django import forms
from .models import ServiceLocation, EnrolledDevice
from .models import Customer
from django.contrib.auth.forms import UserCreationForm

class ServiceLocationForm(forms.ModelForm):
    class Meta:
        model = ServiceLocation
        fields = ['Address', 'UnitNumber', 'MoveInDate', 'SquareFootage', 'Bedrooms', 'Occupants']

class EnrolledDeviceForm(forms.ModelForm):
    class Meta:
        model = EnrolledDevice
        fields = ['ModelId']  # Corrected to match the actual field name in the model

