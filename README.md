# Gas Utility Customer Service Portal http://3.94.113.103:8000

A Django-based web application for managing customer service requests in a gas utility company. This portal allows customers to submit service requests, track their status, and manage their accounts efficiently.

## Features

- **User Authentication**
  - Customer registration and login
  - Secure password management
  - Profile management

- **Service Request Management**
  - Submit new service requests
  - Multiple request types (Gas Leak, New Connection, Billing, Maintenance)
  - File attachment support
  - Real-time status tracking
  - Request history viewing

- **Customer Support**
  - Admin interface for customer support staff
  - Request status management
  - Customer information access
  - Service request tracking

## Technology Stack

- Python 3.11+
- Django 5.1.3
- SQLite Database
- Bootstrap 5.1.3
- HTML/CSS
- JavaScript

## Deployment Stack
- Django 5.1.3
- PM2 for process management
- AWS EC2 t2.micro instance

## Installation

1. Clone the repository
```bash
git clone https://github.com/Jenish2911/Django_Task
cd Django_Task
```

2. Create and activate virtual environment
```bash
# Windows
python -m venv myenv
myenv\Scripts\activate

# macOS/Linux
python -m venv myenv
source myenv/bin/activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```

4. Go into gas_utility_app directory
```bash
cd gas_utility_app
```

5. Set up the database
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser
```bash
python manage.py createsuperuser
```

7. Collect static files
```bash
python manage.py collectstatic
```

8. Run the development server
```bash
python manage.py runserver
```
This will start the server at localhost:8000.

## Deployment
1. Run the above steps to start the server on the AWS EC2 Instance.
Note: To start the server on the EC2 instance run the below command so that the application begins on the EC2 server.
```bash
python manage.py runserver 0.0.0.0:8000
```
This will start the development server at http://{Public IP}:8000/

2. Now to keep the server up and running, I used pm2. Below are the commands to start the server using pm2.
```bash
# Install PM2
npm install pm2 -g

# Start the application
pm2 start ecosystem.config.js

# Monitor the application
pm2 monit

# View logs
pm2 logs gas_utility_app

# Restart the application
pm2 restart gas_utility_ap
```

3. Check whether the server is up and running. If it is, save the pm2 so that even if the EC2 instance is restarted or shut down the server is live.
```bash
# Saves the list of processes managed by pm2. 
pm2 save
```

4. The website is up and running until the EC2 Instance is terminated. (http://3.94.113.103:8000/)

## Application Code Base
```
gas_utility_app/                  # Root project directory
│
├── manage.py                     # Django's command-line utility for administrative tasks
│
├── requirements.txt              # Project dependencies
│
├── .gitignore                   # Git ignore file
│
├── README.md                    # Project documentation
│
├── media/                       # User uploaded files directory
│   └── service_requests/        # Service request attachments
│
├── static/                      # Collected static files
│   ├── admin/                  # Admin static files
│   └── customer_portal/        # App static files
│
├── gas_utility_app/            # Project configuration directory
│   ├── __init__.py            # Python package indicator
│   ├── settings.py            # Project settings
│   ├── urls.py                # Project URL configuration
│   ├── asgi.py               # ASGI configuration for async servers
│   └── wsgi.py               # WSGI configuration for deployment
│
└── customer_portal/           # Main application directory
    ├── __init__.py           # Python package indicator
    │
    ├── admin.py              # Admin interface configuration
    │   # Register models for admin interface
    │   # Configure admin views and customization
    │
    ├── apps.py               # Application configuration
    │   # Define app config class
    │   # Set up app-specific configurations
    │
    ├── forms.py              # Form definitions
    │   # User registration form
    │   # Service request form
    │   # Other form classes
    │
    ├── models.py             # Database models
    │   # Customer model
    │   # ServiceRequest model
    │   # CustomerSupport model
    │
    ├── urls.py               # URL patterns for the app
    │   # Define URL routing
    │   # Map URLs to views
    │
    ├── views.py              # View functions/classes
    │   # Handle HTTP requests
    │   # Process forms
    │   # Render templates
    │
    ├── templates/            # HTML templates
    │   └── customer_portal/
    │       ├── base.html             # Base template with common elements
    │       ├── home.html             # Homepage template
    │       ├── login.html            # Login page template
    │       ├── register.html         # Registration page template
    │       ├── password_change.html  # Password change template
    │       ├── service_request_form.html    # Service request submission template
    │       ├── service_request_list.html    # List of service requests template
    │       └── service_request_detail.html  # Service request details template
    │
    └── static/              # App-specific static files
        └── customer_portal/
            ├── css/         # CSS files
                └── style.css

```

## Models

### Customer
- Linked to Django User model
- Stores customer-specific information
- Includes phone number and address
- Unique customer ID

### ServiceRequest
- Tracks all service requests
- Multiple request types
- Status tracking
- Timestamp information
- File attachment support

### CustomerSupport
- Staff member information
- Department assignment
- Employee ID tracking

## Usage

1. **Customer Registration**
   - Visit the registration page
   - Fill in required information
   - Automatic customer profile creation

2. **Submitting Service Requests**
   - Log in to your account
   - Click "New Request"
   - Select request type
   - Fill in details
   - Attach relevant files (optional)
   - Submit request

3. **Tracking Requests**
   - View all requests in dashboard
   - Check individual request status
   - View request history
   - Download attachments

4. **Admin Access**
   - Login to admin interface
   - Manage users and requests
   - Update request status
   - View customer information

## Admin Interface

Access the admin interface at `/admin` with your superuser credentials to:
- Manage users
- Handle service requests
- View customer information
- Update request status
- Manage support staff

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Database Access

The project uses SQLite database. You can access it through:
1. Django Admin Interface
2. Django Shell
3. DB Browser for SQLite

Example shell queries:
```python
# Access service requests
from customer_portal.models import ServiceRequest
requests = ServiceRequest.objects.all()

# Filter by status
pending = ServiceRequest.objects.filter(status='PENDING')
```

## Security Considerations

- Password hashing using Django's authentication system
- CSRF protection enabled
- Login required for sensitive operations
- File upload validation
- SQLite database file protection

## Contact

Email - jenishmistry2911@gmail.com
Deployment Link - http://3.94.113.103:8000/
