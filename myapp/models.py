from django.db import models
from django.contrib.auth.models import User , AbstractUser ,Group


class Customer(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    LastName = models.CharField(max_length=255)
    FirstName = models.CharField(max_length=255)
    BillingAddress = models.TextField()

class ServiceLocation(models.Model):
    LocationID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Address = models.CharField(max_length=255)
    UnitNumber = models.CharField(max_length=50)
    MoveInDate = models.DateField()
    SquareFootage = models.IntegerField()
    Bedrooms = models.IntegerField()
    Occupants = models.IntegerField()
    zip_code = models.CharField(max_length=10,unique=True)

class DeviceModel(models.Model):
    type_choices = [
        ('AC', 'Air Conditioner'),
        ('Refrigerator', 'Refrigerator'),
        ('Light', 'Light'),
        # Add other types as needed
    ]
    ModelId = models.AutoField(primary_key=True)
    ModelType = models.CharField(max_length=20, choices=type_choices)
    ModelNumber = models.CharField(max_length=255)

class EnrolledDevice(models.Model):
    DeviceId = models.AutoField(primary_key=True)
    LocationId = models.ForeignKey(ServiceLocation, on_delete=models.CASCADE)
    ModelId = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)

class EnergyData(models.Model):
    DataId = models.AutoField(primary_key=True)
    DeviceId = models.ForeignKey(EnrolledDevice, on_delete=models.CASCADE)
    Timestamp = models.DateTimeField()
    Label = models.CharField(max_length=50)
    Value = models.FloatField()

class EnergyPrice(models.Model):
    PriceId = models.AutoField(primary_key=True)
    ZipCode = models.ForeignKey(ServiceLocation, to_field='zip_code', on_delete=models.CASCADE)
    Timestamp = models.DateTimeField()
    Price = models.FloatField()
