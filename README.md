# Restaurant Reservation System

This project is a client-server application for managing table reservations in a restaurant. It allows different types of users to interact with the system, including a reservation attendant, a waiter, and a manager. Each user type has specific functionalities to facilitate the reservation process.

## Project Structure

The project is organized as follows:

```
restaurant-reservation/
├── src/
│   ├── manage.py                # Command-line utility for administrative tasks
│   ├── requirements.txt          # Project dependencies
│   ├── pyproject.toml            # Project metadata and dependencies
│   ├── reservation/              # Reservation app containing models, views, and templates
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── tests.py
│   │   ├── migrations/
│   │   │   └── __init__.py
│   │   ├── templates/
│   │   │   └── reservation/
│   │   │       ├── base.html
│   │   │       ├── attendant.html
│   │   │       ├── waiter.html
│   │   │       ├── manager.html
│   │   │       └── reports.html
│   │   └── static/
│   │       └── reservation/
│   │           └── style.css
│   └── restaurant/               # Main project directory containing settings and configuration
│       ├── __init__.py
│       ├── asgi.py
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
└── .gitignore                    # Files and directories to ignore in version control
```

## Features

- **Reservation Attendant**: Can create and cancel reservations. The attendant inputs details such as date, time, table number, number of people, and the name of the person making the reservation.
  
- **Waiter**: Confirms the occupancy of reserved tables. This updates the status of the table, making it available for future reservations.

- **Manager**: Generates real-time reports on reservations, including:
  - List of reservations attended or not within a specified period.
  - Reservations made for specific tables.
  - Tables confirmed by waiters.

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd restaurant-reservation/src
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

5. **Run migrations**:
   ```
   python manage.py migrate
   ```

6. **Start the development server**:
   ```
   python manage.py runserver
   ```

## Usage

- Access the application through a web browser at `http://127.0.0.1:8000/`.
- Different user interfaces will be available based on the user type (attendant, waiter, manager).

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.