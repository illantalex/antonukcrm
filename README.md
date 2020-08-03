# CRM System

## This is my pet project of the Client Relationship Manager

The actual website is placed [here](https://illantal-crm.herokuapp.com)

It's still in development so that bugs will be fixed and more features will be added

## To run it on your local machine, do the following steps:

1. Clone it on your computer by doing:

    `git clone https://github.com/illantalex/antonukcrm.git`

    `cd antonukcrm`

2. Create and activate a virtual enviromnent:

    `python3 -m venv venv`

    `source venv/bin/activate`

3. Install all requirements:

    `pip install -r requirements.txt`

4. Create database migrations:

    `python3 manage.py migrate`

5. Run local Django server:

    `python3 manage.py runserver`
