# Flask-bootstrap-boilerplate
A boilerplate flask application bootstrappy thinger.  Clone this repo and
you've got a base flask app work on.

## Colophon
- Server side: Python, Flask
- DB: SQL, SQLite, SQL-Alchemy
- Client Side: Bootstrap

## Use
On OS X or Linux (Windows, you're on your own):

### Get code
```sh
$ clone git@gitlab.elevenfifty.com:cameron/$SOME_REPO.git
$ cd ef-flask
```

### Install dependencies
Use a virtualenv.
```sh
$ pip install -r requirements.txt
```

### Settings
```
$ cp secrets.py.example secrets.py
```

Edit `secrets.py` as indicated in the file.  For testing purposes you can
probably get away without editing anything, but a `SECRET_KEY` is suggested.

### Running
To run a development machine:

```sh
$ python manage.py run
```

A dev server will be running on `localhost:5000`.  By going to the address in
your browser you should be able to view a working version of the site. If you'd
like to make the application available to your local network:

```sh
$ python manage.py run_on_network
```

## TODO
- Add License, Copyright, Contrib, etc
    - update all files with info
- add docstrings
- sitemap.xml
- create makefile for this business.


## Basic outline of project
.
├── app
│   ├── api
│   │   ├── controller.py
│   │   └── __init__.py
│   ├── forms.py
│   ├── __init__.py
│   ├── main
│   │   ├── controller.py
│   │   ├── errors.py
│   │   └── __init__.py
│   ├── models.py
│   ├── static
│   │   ├── css
│   │   │   └── style.less
│   │   ├── img
│   │   │   └── favicon.png
│   │   └── js
│   ├── templates
│   │   ├── api
│   │   ├── base.html
│   │   ├── errors
│   │   │   ├── 404.html
│   │   │   └── 500.html
│   │   ├── macros.html
│   │   └── main
│   │       └── index.html
│   └── utils.py
├── base.txt
├── config.py
├── manage.py
├── README.md
├── requirements.txt
├── secrets.py
├── secrets.py.example
├── tests
│   └── __init__.py
├── tmp
├── TOPMATTER.md
└── tree.txt

13 directories, 26 files

mkdir ~/Dev/$APP_NAME
cd ~/Dev/$APP_NAME
mkdir -p app/api
touch app/api/controller.py
touch app/api/__init__.py
touch app/forms.py app/models.py
mkdir app/main app/static
touch app/main/controller.py app/main/__init__.py
mkdir app/static/css app/static/img app/static/js
mkdir app/templates
mkdir app/templates/api
mkdir app/templates/main
mkdir app/templates/errors
touch app/templates/base.html
touch app/utils.py
touch config.py manage.py README.md secrets.py secrets.py.example
mkdir tests
touch tests/__init__.py
mkdir tmp
touch TOPMATTER.md
touch app/main/errors.py
touch app/static/css/style.less
touch app/templates/errors/404.html
touch app/templates/errors/500.html
touch app/templates/main/index.html
