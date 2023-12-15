# SHEMS Web Application

## Overview

SHEMS (Smart Home Energy Management System) is a web application implemented using Django and MySQL. It provides users with functionality related to monitoring and managing energy consumption in their homes.

## Features

### User Authentication

- `/myapp/register`: Allows users to register by entering a username and password.
- `/myapp/login`: Allows users to log into their accounts.
- `/myapp/logout`: Logs users out of their accounts.

### Service Locations

- `/myapp/service-locations`: Lists the user's service locations.
- `/myapp/service-locations/create`: Allows users to add new service locations to their accounts.
- `/myapp/service-locations/<int:pk>/delete/`: Allows users to delete service locations.

### Enrolled Devices

- `/myapp/enrolled-devices`: Users are redirected here after login. This dashboard shows the user's active service locations and enrolled devices at each location.
- `/myapp/enrolled-devices/create`: Allows users to enroll new smart devices.
- `/myapp/enrolled-devices/<int:pk>/delete/`: Allows users to delete enrolled devices.

### Energy Consumption Monitoring

- `/myapp/enrolled_consumption/`: Redirects to a page showing energy consumption for the past month for each service location.
- `/myapp/monitor_consumption/`: Shows the energy consumption for each device at a particular service location in the past month.
- `/myapp/energyprice/`: Shows the current energy prices for each zipcode.
- `/myapp/peakconsumption/`: Shows the device that used the most energy at each service location in the past month.

## Installation

1. Clone the repository: `git clone https://github.com/your-username/SHEMS.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your MySQL database and update the database configurations in `settings.py`.
4. Apply migrations: `python manage.py migrate`
5. Run the development server: `python manage.py runserver`

## Usage

1. Navigate to `http://127.0.0.1:8000/myapp/register/` to register a new user.
2. Log in at `http://127.0.0.1:8000/myapp/login/`.
3. Access the dashboard at `http://127.0.0.1:8000/myapp/enrolled-devices/` after logging in.

## Contributing

Feel free to contribute by opening issues or submitting pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
