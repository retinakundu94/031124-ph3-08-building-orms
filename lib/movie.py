from . import CONN
from . import CURSOR

class Movie:
    def __init__(self, title, year, id=None):
        self.id = id
        self.title = title
        self.year = year

    def __repr__(self):
        return f'Movie(id={self.id}, title={self.title}, year={self.year})'

    # OBJECT RELATIONAL MAPPING / ORM

    # this method creates the table if it doesn't exist...
    @classmethod
    def create_table(cls):
        # first we create the SQL query
        sql = """CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        title TEXT,
        year INTEGER
        )
        """
        # then we execute it
        CURSOR.execute(sql)
        # this is one of the few creative commands that doesn't require a .commit()

    # this command is context sensitive
    def save(self):
        # if the instance exists in the db (it has an id)...
        if self.id:
            # then update it with any changes we've made to the instance
            self.update()
        else:
            # otherwise create it in the db
            self.create()

    # this creates the instance in the db
    def create(self):
        # first we make the sql
        sql = """INSERT INTO movies (title, year)
        VALUES (?, ?)
        """
        # the ?'s get replaced by the arguments in the .execute (first self.title and then self.year)'
        CURSOR.execute(sql, [self.title, self.year])
        # because this is changing a row in the db we commit it
        CONN.commit()
        # last thing! this instance didn't have an official id so we execute some SQL to grab one
        self.id = CURSOR.execute("SELECT * FROM movies ORDER BY id DESC LIMIT 1").fetchone()[0]

    # this updates the db with new info from the instance
    def update(self):
        # before we fire this we would change the year or the title on the isinstance
        # for example movie1.title = "Wolf of Wall Street" followed by movie1.update()
        sql = "UPDATE movies SET title = ?, year = ? WHERE id = ?"
        # below we use a tuple instead of a list but we can use a list (truthfully anything list-like would probably work)
        CURSOR.execute(sql, (self.title, self.year, self.id) )
        # we have to commit now that we've told it what to execute
        CONN.commit()

    # we need a method to fetch all the rows! we'll map them to a new list of instances
    # this is because we want an instance for every row with all the methods and uses an instance entails
    @classmethod
    def get_all(cls):
        # the sql is easy
        sql = "SELECT * FROM movies"
        # we add the .fetch_all() at the end to get a list of tuples
        all_movies = CURSOR.execute(sql).fetchall()
        # finally we go through the list of tuples and return a new list of instances
        movies_list = []
        for movie_data in all_movies:
            movie = Movie(movie_data[1], movie_data[2])
            # we need to make sure the id (movie_data[0]) also gets included
            movie.id = movie_data[0]
            movies_list.append(movie)

        return movies_list

    ### we made two destroy / delete methods ###

    # this first one is a class method that takes in an id
    @classmethod
    def destroy(cls, id):
        # sql executes by plugging the id into the questionmark
        sql = "DELETE FROM movies WHERE id = ?"
        # with a tuple with a length of 1 we need the comma after id
        CURSOR.execute(sql, (id,))
        # and commit
        CONN.commit()

    # here's te same thing but as an instance method ( movie1.destroy() )
    def destroy(self):
        sql = "DELETE FROM movies WHERE id = ?"
        # only difference is that we pass in no id because we can grab self.id
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
