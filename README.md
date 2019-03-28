# Enrollmykid

[![Python|Flask](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Enrollmykid is a cloud-enabled, mobile-ready, offline-storage, Python powered application

# Features!

  - Add a Childcare Centre
  - Update a Childcare Centre
  - View a Childcare Centre
  - Delete a Childcare Centre


You can also:
  - Export centre details as PDF (still in progress)

Markdown is a lightweight markup language based on the formatting conventions that people naturally use in email.  As [John Gruber] writes on the [Markdown site][df1]

### Tech

Enrollmykid uses a number of open source projects to work properly:

* [Python] - HTML enhanced for web apps!
* [Sublime] - awesome text editor
* [markdown-it] - Markdown parser done right. Fast and easy to extend.
* [Bootstrap] - great UI boilerplate for modern web apps


### Installation

Enrollmykid requires [Flask](http://flask.pocoo.org/) to run.

Install the dependencies and devDependencies and start the server.

```sh
$ cd dillinger
$ pyton -m pip install -U -r requirements.txt
$ python app.py
```

For production environments...

```sh
$ export FLASK_CONFIG = production
```
