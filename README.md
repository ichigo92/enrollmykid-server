# Enrollmykid - Server

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Enrollmykid is a cloud-enabled, mobile-ready, Python powered application

**Client** is available at [https://github.com/ichigo92/enrollmykid-client](https://github.com/ichigo92/enrollmykid-client)

# Features!

  - Add a Childcare Centre
  - Update a Childcare Centre
  - View a Childcare Centre
  - Delete a Childcare Centre


You can also:
  - Export centre details as PDF (still in progress)


### Tech

Enrollmykid uses a number of open source projects to work properly:

* [Python] - HTML enhanced for web apps!
* [Sublime] - awesome text editor
* [Bootstrap] - great UI boilerplate for modern web apps


### Installation

Enrollmykid requires [Flask](http://flask.pocoo.org/) to run.

Install the dependencies and devDependencies and start the server.

```sh
$ cd enrollmykid-server
$ python -m pip install -U -r requirements.txt
$ python app.py
```

For production environments...

```sh
$ export FLASK_CONFIG = production
```
