############## IMPORTS ##############

# the . stands for our __init__.py
from . import CONN, CURSOR


############## COURSE ##############

class Course:

    # --- MAGIC METHODS --- #

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"Course(id={self.id}, name={self.name})"

    # --- SQL CLASS METHODS --- #

    @classmethod
    def create_table(cls):
        pass
        # creates the table if it doesn't exist

    @classmethod
    def get_all(cls):
        pass
        # creates a new instance for each row in the db

    @classmethod
    def get_by_id(cls, id):
        pass
        # finds by id and if found instantiates a new instance


    # --- SQL INSTANCE METHODS --- #

    def create(self):
        pass
        # creates in the db and updates instance with the new id


    def update(self):
        pass
        # updates the row based on current attributes 


    def save(self):
        pass
        # creates if it doesn't exist
        # updates if it does exist

    
    def destroy(self):
        pass
        # deletes the instance from the db and removes the id

    # --- JOIN METHODS --- #

    def students(self):
        pass
        # return a list of instances of each student

############## END COURSE ##############



############## STUDENT ##############

class Student:

    # --- MAGIC METHODS --- #

    def __init__(self, name, grade, course_id, id=None):
        self.name = name
        self.grade = grade
        self.id = id
        self.course_id = course_id

    def __repr__(self):
        return f'Student(id={self.id}, name={self.name}, course_id={self.course_id})'
    

    # --- CLASS SQL METHODS --- #

    # make a table if it doesn't exist
    @classmethod
    def create_table(cls):
        pass
        # create table with proper columns if not exists


    # --- SQL METHODS --- #

    def create(self):
        pass
        # add to the database

    def update(self):
        pass
        # update based on current instance attributes

    # remove from the database
    def destroy(self):
        pass
        # destroy row in the db based on id


    # --- SQL CLASS METHODS --- #

    @classmethod
    def get_by_id(cls, id):
        pass
        # find and return instance based on id
        
    # BONUS #
    @classmethod
    def get_by_name(cls, name):
        pass
        # find and return instance based on name
    
    @classmethod
    def get_all(cls):
        pass
        # return all instances from the database


    # --- JOIN METHODS --- #

    def course(self):
        pass
        # get the course by course_id


############## END STUDENT ##############