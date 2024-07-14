# Tweetz

Tweetz is a simple Twitter-like web application built using Django. It allows users to register, log in, and post tweets. Users can also search for specific tweets and edit or delete their own tweets. Unauthenticated users can view the feed in guest mode.

## Features

- **Admin Login**: Admin users can log in and manage the application through the Django admin interface.
- **Custom User Registration**: New users can register and create an account.
- **User Authentication**: Registered users can log in and log out.
- **Guest Mode**: Unauthenticated users can view the feed without logging in.
- **Tweet Management**: Users can create, edit, and delete their own tweets.
- **Search Functionality**: Users can search for specific tweets from all tweets.
- **Frontend**: Built using Python, Django HTML templates, and CSS for styling.

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or later

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/krishp007/Tweetz-Django.git
   cd tweetApp
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python install django
   ```

3. **Make migrations:**
   ```bash
   python manage.py makemigrations
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000`

8. **View Tweets:**
   Open your web browser and go to `http://127.0.0.1:8000/tweet`

## Usage

### Admin Login
- Visit `http://127.0.0.1:8000/admin` to access the Django admin interface.

### Custom User Registration, Login, and Logout
- Register a new user by clicking on the "Register" link on the homepage.
- Log in with your credentials using the "Login" link.
- Log out by clicking the "Logout" button when logged in.

### Guest Mode
- Unauthenticated users can view the tweet feed without logging in.

### Tweet Management
- After logging in, users can create new tweets using the "Create new Tweet" button.
- Users can edit or delete their own tweets by clicking the "Edit" or "Delete" buttons on their tweets.

### Search Functionality
- Use the search bar to find specific tweets by keyword.
