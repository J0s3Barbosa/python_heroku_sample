# Python Web App
```bash
The purpose of this project is create a simple app that uses most concepts used in a web development following MVC architecture, tests and single responsibility principle,

project documentation

also folowing git prectices like
creating branches
commit
PR(pull requests)
merge

```

# Technologies

```bash

- backend
python
Flask
OOP
PIP is a package manager
Python Try Except
JSON
String Formatting
Datetime
Modules
Classes and Objects
If ... Else
Lists
Operators
Booleans
Casting
Variables
Built in Functions


- DataBse
mongoDb - most popular NoSQL database
MongoDB driver "PyMongo"

- Frontend

Jinja2
html
bootstrap4
JavaScript 
AJAX 

https://pypi.org/project/Jinja2/
https://jinja.palletsprojects.com/en/2.11.x/intro/

```

### install requirements

```bash

- upgrade pip
py -m pip install --upgrade pip

install venv
py -m pip install virtualenv

create virtual env
py -m virtualenv venv

activate virtual env
. venv\scripts\activate

install requirements
pip install -r requirements.txt

```

## How to run

```bash
$ python main.py
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### upgrade requirements

```bash

pip install -r requirements.txt --upgrade


pip list --outdated
pip freeze > requirements.txt
pip install -r requirements.txt --upgrade

import pkg_resources
from subprocess import call

for dist in pkg_resources.working_set:
    call("python -m pip install --upgrade " + dist.<projectname>, shell=True)

```
