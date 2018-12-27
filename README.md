# Python Web Application

[![Travis Build](https://img.shields.io/travis/endormi/python-webapp-list.svg?style=flat-square)](https://travis-ci.org/endormi/python-webapp-list)
[![python version](https://img.shields.io/badge/python-3.7.1-brightgreen.svg?style=popout-square)](https://www.python.org/downloads/)
[![django version](https://img.shields.io/badge/django-2.1.3-brightgreen.svg?style=popout-square)](https://www.djangoproject.com/download/)

[Badges](https://shields.io/#/)

> Python To-Do List. Very simple. 

## Running the Project Locally

Clone the repository to your local machine:

```
git clone https://github.com/endormi/python-webapp-list.git
```

Create the database:

```
python manage.py migrate
```

Run the development server:

```
python manage.py runserver
```

Project will be available at **127.0.0.1:8000**

### Local Users

Creating a local [user](https://github.com/endormi/python-webapp/blob/master/USERS):

```
python manage.py createsuperuser
```

Test user at **127.0.0.1:8000/admin**

### Testing

Click [here](https://github.com/endormi/python-webapp-list/blob/master/TESTS) to see what I use for testing.

### Running .travis.yml test

```
python manage.py test travis
```

## License

The source code is released under the [MIT License](https://github.com/endormi/python-webapp-list/blob/master/LICENSE).
