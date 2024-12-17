# Airline Booking System with Python and Django

## Overview

This project is an Airline Booking System built with Python and Django. It allows users to view available flights, see flight details, add passengers to flights, and manage their accounts.

## How to Run the Project

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Jaweria-B/airline
   ```

2. Navigate to the project directory:

   ```bash
   cd airline
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Apply database migrations:

   ```bash
   python manage.py migrate
   ```

4. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

5. Open your web browser and use the following URLs:

   - **View Flights:** Go to `/flights` to see all available flights.
   - **Flight Details:** Click on any flight to see complete details, including enrolled passengers or to add new passengers to the flight.
   - **User Login:** Go to `/users/login` to log in to your account.
   - **User Account:** Go to `/users` to view your account information.

## Requirements

- Python 3.x
- Django (install using `pip install django`)

## Features

- View all available flights.
- See detailed flight information, including a list of passengers.
- Add passengers to flights.
- User login and account management.

Enjoy managing flight bookings with this robust and user-friendly application!
