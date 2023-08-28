from . import CONN
from . import CURSOR
from .course import Course

class Student:

    # --- MAGIC METHODS --- #

    def __init__(self, name, grade, course_id, id=None):
        self.name = name
        self.grade = grade
        self.id = id
        self.course_id = course_id

    def __repr__(self):
        return f'Student(id={self.id}, name={self.name}, course_id={self.course_id})'
    

    # --- JOIN PROPERTIES --- #

    @property
    def course(self):
        sql = """SELECT * FROM courses WHERE id = ?
        """

        co_tuple = CURSOR.execute(sql, [self.course_id]).fetchone()
        if co_tuple:
            return Course(id=co_tuple[0], name=co_tuple[1])

    @course.setter
    def course(self, course):
        if type(course) == Course:
            self.course_id = course.id


    # --- CLASS SQL METHODS --- #

    # make a table if it doesn't exist
    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            grade NUMBER,
            course_id INTEGER
            )
        """

        return CURSOR.execute(sql)


    # --- SQL METHODS --- #

    # add this to the database
    def create(self):
        sql="""INSERT INTO students (name, grade, course_id) 
        VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, [self.name, self.grade, self.course_id])
        CONN.commit()

        sql="""SELECT * FROM students
        WHERE id = last_insert_rowid() 
        """

        student_tuple = CURSOR.execute(sql).fetchone()
        id = student_tuple[0]

        self.id = id

        # save changes to the database
    def update(self):
        sql="""UPDATE students
        SET name = ?, grade = ?, course_id = ?
        WHERE id = ?
        """

        CURSOR.execute(sql, [self.name, self.grade, self.course_id, self.id])
        CONN.commit()


    # get a row by id and map it into an instance
    @classmethod
    def get_by_id(cls, id):
        sql = """SELECT * FROM students
        WHERE id = ?
        """

        st_tuple = CURSOR.execute(sql, [id]).fetchone()
        return Student(name=st_tuple[1], grade=st_tuple[2], id=st_tuple[0], coures_id=st_tuple[3])
        
    # get a row by id and map it into an instance
    @classmethod
    def get_by_name(cls, name):
        sql = """SELECT * FROM students
        WHERE name = ?
        """

        st_tuple = CURSOR.execute(sql, [name]).fetchone()
        return Student(name=st_tuple[1], grade=st_tuple[2], id=st_tuple[0], course_id=st_tuple[3])
    
    # get all rows and map them into instances
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM students"

        student_tuples = CURSOR.execute(sql).fetchall()

        return [Student(name=student[1], grade=student[2], id=student[0], course_id=student[3]) for student in student_tuples]
        

    # remove from the database
    def destroy(self):
        sql="""DELETE FROM students
        WHERE id = ?
        """

        CURSOR.execute(sql, [ self.id ])
        CONN.commit()