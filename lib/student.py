from . import CONN
from . import CURSOR

class Student:

    # --- MAGIC METHODS --- #

    def __init__(self, name, grade, id=None):
        self.name = name
        self.grade = grade
        self.id = id

    def __repr__(self):
        return f'Movie(id={self.id}, title={self.title}, year={self.year})'

    # --- CLASS METHODS --- #

    # make a table if it doesn't exist
    @classmethod
    def create_table(cls):
        pass

    # get all rows and map them into instances
    @classmethod
    def get_all(cls):
        pass

    # get a row by id and map it into an instance
    @classmethod
    def get_by_id(cls, id):
        pass

    # --- SQL METHODS --- #

    # add this to the database
    def create(self):
        pass

    # save changes to the database
    def update(self):
        pass

    # remove from the database
    def destroy(self):
        pass
