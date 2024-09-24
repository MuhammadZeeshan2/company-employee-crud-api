# Company & Employee Management API

This project is a Django REST Framework-based API for managing companies and employees. The API allows CRUD operations on companies and employees, with a relationship between companies and their employees.

## Table of Contents
- [Setup](#setup)
- [Features](#features)
- [API Endpoints](#api-endpoints)
- [Models](#models)
- [How to Use](#how-to-use)
- [Contributing](#contributing)

## Setup

### 1. Clone the Repository:

$ git clone https://github.com/MuhammadZeeshan2/company-employee-crud-api.git
$ cd companyapi



2. Create a Virtual Environment:

$ python3 -m venv .env
$ source .env/bin/activate
3. Install Dependencies:

$ pip install -r requirements.txt
4. Make Migrations:


$ python manage.py makemigrations
5. Run Migrations:


$ python manage.py migrate
6. Start the Development Server:


$ python manage.py runserver
Now, navigate to http://127.0.0.1:8000/api/v1/ to interact with the API.