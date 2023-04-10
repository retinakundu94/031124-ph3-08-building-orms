from . import CONN
from . import CURSOR

class Movie:
    def __init__(self, title, year, id=None):
        self.id = id
        self.title = title
        self._year = year

    def __repr__(self):
        return f'<Movie id={self.id} title={self.title} year={self.year}>'

    def get_year(self):
        return self._year

    def set_year(self, year):
        if year >= 2000 and isinstance(year, int):
            self._year = year
        else:
            print("That movie is too old and doesn't matter")

    year = property(get_year, set_year)

    # OBJECT RELATIONAL MAPPING / ORM

    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        title TEXT,
        year INTEGER
        )
        """
        CURSOR.execute(sql)

    def save(self):
        if self.id:
            self.update()
        else:
            self.create()

    def create(self):
        sql = """INSERT INTO movies (title, year)
        VALUES (?, ?)
        """
        CURSOR.execute(sql, [self.title, self.year])
        CONN.commit()
        self.id = CURSOR.execute("SELECT * FROM movies ORDER BY id DESC LIMIT 1").fetchone()[0]

    def update(self):
        sql = "UPDATE movies SET title = ?, year = ? WHERE id = ?"
        CURSOR.execute(sql, (self.title, self.year, self.id) )
        CONN.commit()

    @classmethod
    def fetch_all(cls):
        sql = "SELECT * FROM movies"
        all_movies = CURSOR.execute(sql).fetchall()
        movies_list = []
        for movie_data in all_movies:
            movie = Movie(movie_data[1], movie_data[2])
            movie.id = movie_data[0]
            movies_list.append(movie)

        return movies_list

    @classmethod
    def destroy(cls, id):
        sql = "DELETE FROM movies WHERE id = ?"
        CURSOR.execute(sql, (id,))
        CONN.commit()

    def destroy(self):
        sql = "DELETE FROM movies WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
