from . import CONN
from . import CURSOR

class Movie:
    def __init__(self, title:str, year:int, id:int=None):
        self.id = id
        self.title = title
        self.year = year

    def __repr__(self):
        return f'Movie(id={self.id}, title={self.title}, year={self.year})'


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
    def get_by_id(cls, id:int):
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