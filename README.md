# PythonTools

# Technologies
python
mongoDb 

## Environment

```bash
pip install -r requirements.pip
```

## How to run

```bash
$ python todo.py
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
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
