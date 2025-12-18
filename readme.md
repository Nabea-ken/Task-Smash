# Making a CRUD APP

-Flask, Sass, SQLAlchemy

## What to learn

1. Understanding Basic Operations
    -Ideation Process:
        -Basic Setup
            *Virtual Env
            *Packages and Dependencies
            *Initial Flask App
            *Project Structure and setup
            *Link HTML files
            *Link CSS files
            *Testing
        -Create a Database Model
            -Create a Model-->a model is a row of data in our db, this will collect and hold data for each item
            *flask SQLAlchemy configure the extension
        -HTTP Methods and functionality
            *Add a task to the db (POST)
            *Delete a task from the db
            *Edit a task in the db (GET/POST)
        -Styling with SASS and finalize app
            -Add any and all CSS styling
            -Finalize any final ideas
2. Hands-on Experience
3. Database Interaction --> SQL
4. Learn HTTP Methods
5. Transferable skills
6. New Frameworks and tech

-Deployment
python anywhere
create a new app
console
    *mkvirtualenv myvirtualenv --python=/usr/bin/python3.10
    *git clone <https://github.com/Nabea-ken/Task-Smash.git>
    *cd Task-Smash
    *pip install -r requirements.txt

-Earlier one i created with python3.10 which caused an error on pythonanywhere
  so i had to create another venv
    *rm -rf myvirtualenv
    *python3.13 -m venv Smash
    *source Smash/bin/activate
    *pip install -r requirements.txt

-setup source code url

-setup WSGI configuration file
    import sys
    path = '/home/knabz/Task-Smash'
    if path not in sys.path:
     sys.path.append(path)

    from app import app as application

setup virtualenv path
refresh
click link to view your web app

[EOF]
