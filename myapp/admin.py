

from django.contrib import admin
from .models import User,Customer, ServiceLocation, DeviceModel, EnrolledDevice, EnergyData, EnergyPrice


admin.site.register(Customer)
admin.site.register(ServiceLocation)
admin.site.register(DeviceModel)
admin.site.register(EnrolledDevice)
admin.site.register(EnergyData)
admin.site.register(EnergyPrice)
