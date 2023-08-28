# SQL Fundamentals and SQLite3 in Python

## Learning Goals

- Python architecture with `__init__.py` and the `Pipfile`

- CRUD using SQL queries

  - CREATE TABLE

  - INSERT INTO

  - SELECT FROM

  - UPDATE SET

  - DELETE FROM

- The SQLite3 package in Python

- Sending SQL commands using CURSOR and CONN

- What is an ORM

- Building an ORM in Python

## Getting Started

Fork and clone. In the terminal run `pipenv install` followed by `pipenv shell`. You should be able to debug easily with `python3 debug.py`. If the `ipdb` isn't working then remove it and run `python3 -i debug.py`.

## Exercises

Build out the predefined empty methods in the `Movie` class in `movie.py`.

BONUS: Create a `destroy_by_id` class method. When called, it takes in an id as an argument and deletes the row with that id.

BONUS: Create a `save()` instance method. When called, it will either call the `create` or the `update` method depending on whether the instance is already in the database (essentially whether the instance has an id or not).
