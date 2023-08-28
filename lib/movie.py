from . import CONN
from . import CURSOR

class Movie:
    def __init__(self, title, year, id=None):
        self.id = id
        self.title = title
        self.year = year

    def __repr__(self):
        return f'Movie(id={self.id}, title={self.title}, year={self.year})'


    # --- SQL CLASS METHODS --- #

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
        sql="SELECT * FROM movies"

        movie_tuples = CURSOR.execute(sql).fetchall()
        return [ Movie(title=movie[1], year=movie[2], id=movie[0]) for movie in movie_tuples ]


    @classmethod
    def destroy_by_id(cls, id):
        sql = "DELETE FROM movies WHERE id = ?"

        CURSOR.execute(sql, [ id ])
        CONN.commit()


    @classmethod
    def get_by_id(cls, id):
        sql="""SELECT * FROM movies
        WHERE id = ?
        """

        tuple = CURSOR.execute(sql, [id]).fetchone()

        if tuple:
            return Movie(id=tuple[0], title=tuple[1], year=tuple[2])


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
        sql="""UPDATE movies
        SET title = ?, year = ?
        WHERE id = ?
        """

        CURSOR.execute(sql, [ self.title, self.year, self.id ])
        CONN.commit()


    def save(self):
        if self.id:
            self.update()
        else:
            self.create()

    
    def destroy(self):
        sql="""DELETE FROM movies
        WHERE id = ?
        """

        CURSOR.execute(sql, [self.id])
        CONN.commit()