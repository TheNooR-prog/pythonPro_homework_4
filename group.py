import custom_extantions
import logging
import studentclass

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime) s %(name)-12s %(levelname)-8s %(message)s')

filehandler = logging.FileHandler(f'{__name__}.log')
filehandler.setLevel(logging.INFO)
filehandler.setFormatter(formatter)

streamhandler = logging.StreamHandler()
streamhandler.setLevel(logging.WARNING)
streamhandler.setFormatter(formatter)

logger.addHandler(filehandler)
logger.addHandler(streamhandler)

class Group:

    def __init__(self, title, students_limit = 10):
        self.title = title
        self.students_limit = students_limit
        self.__students = []

    def add_student(self, student : studentclass.Student):
        if not isinstance(student, studentclass.Student):
            logger.warning(f'{student}: Wrong data type with student')
            raise TypeError("Student is not an instance of class Student")
        if student in self.__students:
            logger.warning(f'{student}: Duplicat of student')
            raise ValueError("Student is already in list")
        if len(self.__students) >= self.students_limit:
            logger.warning(f'{student}: Limit')
            raise custom_extantions.StudentsLimit(f"Limit is {self.students_limit}")

        logger.info(f'{student}: Added')
        self.__students.append(student)

    def __str__(self):
        return f"{self.title}\n" + "\n".join(map(str, self.__students))