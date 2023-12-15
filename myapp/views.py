from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Customer, ServiceLocation, DeviceModel, EnrolledDevice, EnergyData, EnergyPrice, User
from .forms import ServiceLocationForm, EnrolledDeviceForm 
from django.urls import reverse


# User authentication views

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # This line saves the user to the database
            login(request, user)
            return redirect(reverse_lazy('login'))  # Redirect to the dashboard or another page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            return redirect('enrolled_devices')  # Redirect to enrolled_device_list after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

@login_required
def enrolled_device_view(request):
    user_id = request.user.id
    
    # Retrieve the user object from the User model
    user = User.objects.get(id=user_id)
    
    # Now you can access the user's name
    user_name = user.username
    print(user_name)
    print(user_id)
    
    
   

    # Assuming you have a ServiceLocation model with a ForeignKey to User
    # Adjust the model and field names based on your actual model structure
    locations = ServiceLocation.objects.filter(CustomerID=user_id)
  
    # Create a dictionary to store addresses
    address_dict = {}
    i=1
    for location in locations:
        
        address_dict[f'address{i}'] = location.Address
        i=i+1

    return render(request, 'enrolled_device_list.html', {'user_name': user_name, **address_dict})


def enrolled_consumption(request):
    # Your logic for energy consumption view goes here
    user_id = request.user.id
    
    # Retrieve the user object from the User model
    user = User.objects.get(id=user_id)
    
   
    user_name = user.username
    print(user_name)
    print(user_id)
    return render(request, 'enrolled_consumption.html')



def monitor_consumption(request):
    # Your logic for energy consumption view goes here
    user_id = request.user.id
    
    # Retrieve the user object from the User model
    user = User.objects.get(id=user_id)
    
   
    user_name = user.username
    print(user_name)
    print(user_id)
    return render(request, 'monitor_consumption.html')


def energyprice(request):
    # Your logic for energy consumption view goes here
    user_id = request.user.id
    
    # Retrieve the user object from the User model
    user = User.objects.get(id=user_id)
    
   
    user_name = user.username
    print(user_name)
    print(user_id)
    return render(request, 'energyprice.html')

def peak_consumption(request):
    # Your logic for energy consumption view goes here
    user_id = request.user.id
    
    # Retrieve the user object from the User model
    user = User.objects.get(id=user_id)
    
   
    user_name = user.username
    print(user_name)
    print(user_id)
    return render(request, 'peakconsumption.html')
from django.shortcuts import render
from django.db.models import Sum
from .models import ServiceLocation, EnrolledDevice, EnergyData

def peak_consumption_view(request, location_id):
    # Get the location
    location = ServiceLocation.objects.get(LocationID=location_id)

    # Get all enrolled devices at the specified location
    enrolled_devices = EnrolledDevice.objects.filter(LocationId=location)

    # Dictionary to store device-wise total energy consumption
    device_data = {}

    for enrolled_device in enrolled_devices:
        device_id = enrolled_device.DeviceId

        # Fetch energy data for the enrolled device
        energy_data_entries = EnergyData.objects.filter(DeviceId=device_id)

        # Calculate total energy consumption for the device
        total_consumption = sum(entry.Value for entry in energy_data_entries)

        # Store the result in the dictionary
        device_data[enrolled_device.ModelId.ModelType] = total_consumption

    # Find the device with the maximum consumption
    highest_consumed_device = max(device_data, key=device_data.get)
    highest_consumed_value = device_data[highest_consumed_device]

    # Pass the data to the template
    context = {
        'location': location,
        'highest_consumed_device': highest_consumed_device,
        'highest_consumed_value': highest_consumed_value,
    }

    return render(request, 'highest_consumed_device.html', context)


from django.shortcuts import render
from .models import EnergyPrice

def energyprice_view(request):
    # Fetch energy prices from the EnergyPrice model
    energy_prices = EnergyPrice.objects.all()

    # Create lists to store zip codes and corresponding prices
    zip_codes = []
    prices = []

    # Extract data from the queryset
    for energy_price in energy_prices:
        zip_codes.append(str(energy_price.ZipCode.zip_code))
        prices.append(energy_price.Price)

    # Prepare data for rendering in the template
    data = {
        'zip_codes': zip_codes,
        'prices': prices,
    }

    return render(request, 'energyprice_view.html', data)


def monitor_consumption_view(request, location_id):
    # Assuming you have a valid location_id in the request

    # Fetch enrolled devices for the specified location
    enrolled_devices = EnrolledDevice.objects.filter(LocationId=location_id)

    # Dictionary to store device-wise energy consumption
    device_data = {}

    # Iterate through enrolled devices
    for enrolled_device in enrolled_devices:
        device_id = enrolled_device.DeviceId

        # Fetch energy data for the enrolled device
        energy_data_entries = EnergyData.objects.filter(DeviceId=device_id)

        # Extract labels and values for the chart
        labels = [entry.Label for entry in energy_data_entries]
        values = [entry.Value for entry in energy_data_entries]

        # Store the result in the dictionary
        device_data[enrolled_device.ModelId.ModelType] = {'labels': labels, 'values': values}

    return render(request, 'monitor_consumption.html', {'device_data': device_data})

@login_required
def enrolled_consumption_view(request):
    # Assuming user is logged in
    location_id=1
    user = request.user

    # Fetch enrolled devices for the specified location and user
    enrolled_devices = EnrolledDevice.objects.filter(LocationId=location_id)

    # Dictionary to store location-wise device-wise energy consumption
    location_data = {}
    
    for enrolled_device in enrolled_devices:
        device_id = enrolled_device.DeviceId
        location = enrolled_device.LocationId

        # Fetch energy data for the enrolled device
        energy_data_entries = EnergyData.objects.filter(DeviceId=device_id)

        # Calculate energy consumption for each device in the location
        for entry in energy_data_entries:
            device_type = entry.DeviceId.ModelId.ModelType
            consumption = entry.Value

            # Initialize the dictionary if not exists
            if location.Address not in location_data:
                location_data[location.Address] = {}

            # Store the consumption for each device in the dictionary
            location_data[location.Address][device_type] = location_data[location.Address].get(device_type, 0) + consumption

    return render(request, 'enrolled_consumption.html', {'location_data': location_data})



# CRUD views for ServiceLocation
class ServiceLocationListView(ListView):
    model = ServiceLocation
    template_name = 'service_location_list.html'

class ServiceLocationCreateView(CreateView):
    model = ServiceLocation
    form_class = ServiceLocationForm
    template_name = 'service_location_form.html'
    success_url = reverse_lazy('service_location_list')

class ServiceLocationDeleteView(DeleteView):
    model = ServiceLocation
    template_name = 'service_location_confirm_delete.html'
    success_url = reverse_lazy('service_location_list')

# CRUD views for EnrolledDevice
# def enrolled_device_view(request):
#     model = EnrolledDevice
#     template_name = 'enrolled_device_list.html'
#     context_object_name = 'enrolled_devices'  # Optional: specify the variable name in the template
#     return render(request, 'enrolled_device_list.html')
#     def get_queryset(self):
#         # Get the LocationId from the request or any other source
#        # location_id = self.request.GET.get('location_id')  # Adjust as needed
#         location_id=1

#         # Filter EnrolledDevice objects based on LocationId
#         queryset = EnrolledDevice.objects.filter(LocationId=location_id)
#         return queryset
class EnrolledDeviceCreateView(CreateView):
    model = EnrolledDevice
    form_class = EnrolledDeviceForm
    template_name = 'enrolled_device_form.html'
    success_url = reverse_lazy('enrolled_device_list')

class EnrolledDeviceDeleteView(DeleteView):
    model = EnrolledDevice
    template_name = 'enrolled_device_confirm_delete.html'
    success_url = reverse_lazy('enrolled_device_list')

# Energy consumption views


