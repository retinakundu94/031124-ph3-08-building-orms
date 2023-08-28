from . import CONN, CURSOR

class Course:

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"Course(id={self.id}, name={self.name})"

    # add in all the other jazz you would need for courses here! #

    # --- JOIN PROPERTIES --- #

    @property
    def students(self):
        sql="""SELECT * FROM students WHERE course_id = ?
        """

        student_tuples = CURSOR.execute(sql, [self.id]).fetchall()

        return [Student(id=student[0], name=student[1], grade=student[2], course_id=student[3]) for student in student_tuples]
    
    @students.setter
    def students(self, whatever):
        raise "May not set the students here"