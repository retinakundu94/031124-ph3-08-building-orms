from . import CONN
from . import CURSOR

class Movie:
    def __init__(self, title, year, id=None):
        self.id = id
        self.title = title
        self.year = year

    def __repr__(self):
        return f'Movie(id={self.id}, title={self.title}, year={self.year})'

    # --- CLASS METHODS --- #

    @classmethod
    def create_table(cls):
        sql="""CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        title TEXT,
        year NUMBER
        )
        """

        return CURSOR.execute(sql)
        # CONN.commit()








    @classmethod
    def get_all(cls):
        pass

    # BONUS: this will destroy a row based on a given id
    @classmethod
    def destroy_by_id(cls, id):
        pass


    # --- SQL INSTANCE METHODS --- #

    def create(self):
        sql="""INSERT INTO movies (title, year) 
        VALUES (?, ?)
        """

        CURSOR.execute(sql, [self.title, self.year])
        CONN.commit()

        sql="SELECT last_insert_rowid() FROM movies "

        movie_tuple = CURSOR.execute(sql).fetchone()

        self.id = movie_tuple[0]









    def update(self):
        pass

    # BONUS: this will either create or update depending on if this instance exists in the db
    def save(self):
        pass

    def destroy(self):
        pass
