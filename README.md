# Mock Social Network

## Description

This is a Python Flask REST API mock dating platform in which users can register, login, logout, set up a profile, search
for users by name, location, age, sex, message other users and view messages. It also features alembic migrations.

## Installation

Clone the repository locally
````bash
git clone <url>
````
Install the outer libraries using the `requirements.txt` file that is part of the project:
````bash
pip install -r requirements.txt
````
The solution counts mainly on Flask workframe and additional Flask libraries. Migrations for the DataBase are available through `Flask-Migrate`.
Any secrets are included in a `settings.ini` file. Please check [Configuration] for more details.
The endpoints' data is generated through `Postman`.

Python version -> 3.9

## Configuration

Access information should be provided in a `settings.ini` file that is not committed to the repository since it holds all secrets.
The file has the following structure:

````
[settings]
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DB_NAME=
SECRET_KEY=
````

## Developed by
`nkonstnikolov@gmail.com` - Nikolay Nikolov