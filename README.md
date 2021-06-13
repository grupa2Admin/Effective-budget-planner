
Effective-budget-planner app
Our app is a simple budget application built with Django. It's designed to manage your personal finances. You can add your expenses, income and even manage your more important receipts. We used Django 3.2.3 version and Python 3.8.


Setup

The first thing to do is clone the repository:
https://github.com/grupa2Admin/Effective-budget-planner.git

Create a virtual environment to install dependencies and activate it:

$ virtualenv2 --no-site-packages env
$ source env/bin/activate

Then install the dependencies:

(env)$ pip install -r requirements.txt

Once pip has finished downloading install the dependencies below:

(env)$ cd project
(env)$ python manage.py runserver

And navigate to http://127.0.0.1:8000/
