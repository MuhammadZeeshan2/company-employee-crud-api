

# Introduction:Company & Employee Management API


This project provides a Django REST Framework-based API for managing companies and employees. It allows CRUD operations on companies and employees, with a relationship between companies and their employees.

![API Overview](__screenshots/api-overview.png?raw=true "API Overview")

### Main Features

* CRUD operations on companies and employees
* Relationship management between companies and employees
* Django REST Framework-based for easy API development
* Supports SQLite or other databases
### Existing virtualenv

If your project is already in an existing Python3 virtual environment, first install Django and Django REST Framework by running:

    $ pip install django djangorestframework

Then, clone the repository and follow the setup steps below:

    $ git clone https://github.com/MuhammadZeeshan2/company-employee-crud-api.git
    $ cd companyapi
    
### No virtualenv

This assumes that `python3` is linked to a valid installation of Python 3 and that `pip` is installed.

If you don't have Django installed for Python 3, run:

    $ pip3 install django djangorestframework
    
Clone the repository:

    $ git clone https://github.com/MuhammadZeeshan2/company-employee-crud-api.git
    $ cd companyapi
    
After that, install the local dependencies, run migrations, and start the server.Follow the commands given below for these previously mentioned actions.


### Create and Activate Virtual Environment

#### On Windows:
1. Create the virtual environment:
    ```bash
    python -m venv .env
    ```

2. Activate the virtual environment:
    ```bash
    .env\Scripts\activate
    ```

#### On Linux/MacOS:
1. Create the virtual environment:
    ```bash
    python3 -m venv .env
    ```

2. Activate the virtual environment:
    ```bash
    source .env/bin/activate
    ```
    
### Install project dependencies:

    $ pip install -r requirements.txt
    
### Apply the migrations:

    $ python manage.py makemigrations
    $ python manage.py migrate
    
### Start the development server:

    $ python manage.py runserver

You can now interact with the API at: 

    http://127.0.0.1:8000/api/v1/
