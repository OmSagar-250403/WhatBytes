# Authentication System

This is an authentication system web application built using Django. It provides essential features like user registration, login, password reset, and password change. It's designed to offer a secure and user-friendly experience for handling authentication in web applications.

---

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Technologies](#technologies)
5. [Contributing](#contributing)
6. [License](#license)

---

## Installation

Follow these steps to set up and run the authentication system locally:

### Prerequisites

- Python 3.x
- Django 3.x or later
- A code editor (like VSCode or PyCharm)
- Virtualenv (optional but recommended)

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/OmSagar-250403/WhatBytes.git
    cd project
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

4. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser (optional for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Access the app:**

    Open your browser and go to:

    ```
    http://127.0.0.1:8000
    ```

---

## Usage

- **Register a new account**: Go to the registration page to create a new user.
- **Login**: After registration, you can log in using your credentials.
- **Password Reset**: If you forget your password, you can reset it via the password reset page.
- **Dashboard**: Once logged in, you'll be redirected to the dashboard page.
- **Logout**: You can log out from the dashboard or any page when logged in.

---

## Features

- **User Registration**: Users can sign up with a username, email, and password.
- **User Login**: Registered users can log in to access secured pages.
- **Password Reset**: Users can reset their password via email if they forget it.

---

## Technologies

- **Backend**: Django (Python Web Framework)
- **Frontend**: HTML, CSS, Bootstrap 4 (for UI)
- **Database**: SQLite (default; can be switched to others like PostgreSQL or MySQL)
- **Authentication**: Django's built-in authentication system

---

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a new Pull Request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Thanks to the Django community for their amazing documentation and support.
- Bootstrap for providing easy-to-use UI components.

