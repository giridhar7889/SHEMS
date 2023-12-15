# your_app/urls.py
from django.urls import path
from .views import (
    register_view, login_view, logout_view,
    ServiceLocationListView, ServiceLocationCreateView, ServiceLocationDeleteView,
   EnrolledDeviceCreateView, EnrolledDeviceDeleteView,
   enrolled_device_view,enrolled_consumption,enrolled_consumption_view,monitor_consumption,energyprice,peak_consumption
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('service-locations/', ServiceLocationListView.as_view(), name='service_location_list'),
    path('service-locations/create/', ServiceLocationCreateView.as_view(), name='service_location_create'),
    path('service-locations/<int:pk>/delete/', ServiceLocationDeleteView.as_view(), name='service_location_delete'),

    path('enrolled-devices/', enrolled_device_view,name='enrolled_devices'),
    path('enrolled-devices/create/', EnrolledDeviceCreateView.as_view(), name='enrolled_device_create'),
    path('enrolled-devices/<int:pk>/delete/', EnrolledDeviceDeleteView.as_view(), name='enrolled_device_delete'),

    path('enrolled_consumption/<int:location_id>/', enrolled_consumption_view, name='enrolled_consumption_view'),
    path('enrolled_consumption/', enrolled_consumption, name='enrolled_consumption'),
    path('monitor_consumption/', monitor_consumption, name='monitor_consumption'),
    path('energyprice/', energyprice, name='energyprice'),
    path('peakconsumption/', peak_consumption, name='peak_consumption')
    # Add more URLs for additional views as needed
]
