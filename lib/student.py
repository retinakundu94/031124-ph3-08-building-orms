from . import CONN
from . import CURSOR

class Student:

    # --- MAGIC METHODS --- #

    def __init__(self, name, grade, id=None):
        self.name = name
        self.grade = grade
        self.id = id

    def __repr__(self):
        return f'Student(id={self.id}, name={self.name}, grade={self.grade})'

    # --- CLASS METHODS --- #

    # make a table if it doesn't exist
    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            grade NUMBER
            )
        """

        return CURSOR.execute(sql)


















    # --- SQL METHODS --- #

    # add this to the database
    def create(self):
        sql="""INSERT INTO students (name, grade) 
        VALUES (?, ?)
        """

        CURSOR.execute(sql, [self.name, self.grade])
        CONN.commit()

        sql="""SELECT * FROM students
        WHERE id = last_insert_rowid() 
        """

        student_tuple = CURSOR.execute(sql).fetchone()
        id = student_tuple[0]

        self.id = id










    # save changes to the database
    def update(self):
        pass

    # remove from the database
    def destroy(self):
        pass













    # get all rows and map them into instances
    @classmethod
    def get_all(cls):
        pass

    # get a row by id and map it into an instance
    @classmethod
    def get_by_id(cls, id):
        pass