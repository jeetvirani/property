# Buzztime

Buzztime - A project to create ultimate bar and restaurant entertainment experience.

##Steps to Setup Local Environment.

###To setup local environment dependencies

1. Install python3.
   Ubuntu :- sudo apt-get install python3
   Mac:- brew install python3
2. See if it works and show version as 3.x.x
   python3
3. Install python3-dev (for ubuntu users)
   sudo apt-get install python3-dev
4. Install unixodbc-dev(for ubuntu users)
   sudo apt-get install unixodbc-dev
5. Install python-virtualenv
   Ubuntu :- sudo apt-get install python-virtualenv
   Mac:- sudo pip install virtualenv
6. Create virtual environment.(please change 3.4 to your python version)
   Ubuntu :- virtualenv pyvenv
   Mac :- virtualenv yourenv -p python3.4
7. Set its path (please change 3.4 to your python version) (for ubuntu users)
   virtualenv -p /usr/bin/python3.4 pyvenv
8. Activate it.
   source pyvenv/bin/activate
9. Create env variable file give name as .env specified all env values. run below command to export it.
   export $(cat .env)
10. Install dependencies:
    pip3 install -r requirements.txt

###To run the project on local

1. Run virtualenv:
   Move to the project directory and execute
   `source pyvenv/bin/activate`
2. Create a file as `.env` and copy all the environmental variables listed in Documentation.
3. Create `out` folder by executing `mkdir out`.
4. To use sqlite3 as DB:
   Change environment variable CONNECT_DB to False
5. Export Environmental Variables
   `export $(cat .env)`
6. Run Migrations:
   `python manage.py migrate`
7. Create SuperUser:
   `python manage.py createsuperuser`
8. Run Server:
   `python manage.py runserver`
9. Access Django Admin:
   Hit `127.0.0.1:8000/api/admin` in browser and provide your superuser credentials.

###Adding Customized Data
One can add directly using Django Admin running at `127.0.0.1:8000/api/admin`

###To run the server

1. python3 manage.py runserver

###To run test cases

1. Running all test cases
   `python3 manage.py test`
2. Run a particular test file
   `python manage.py test <folder.module.filename.Classname.specific function name>`

###For code Coverage

1. Install Coverage <br>
   `pip3 install coverage==4.4.2`
2. To generate coverage file <br>
   `coverage run --rcfile=.coveragerc manage.py test property`
3. To generate coverage report <br>
   After step-1 run<br>
   `coverage html --rcfile=.coveragerc --omit */<your_virtual_env_name>/*`<br>
   It will generate coverage folder in /out
