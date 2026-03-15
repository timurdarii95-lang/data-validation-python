from email.policy import default
from pydantic import BaseModel

from fastapi import FastAPI, Body
from pydantic import BaseModel
from sorin.courses import Course

app = FastAPI()

COURSES = [
    Course(1,
           'Matematics',
           'Jhon Smith',
           'Fundamentals of maths',
           4
    ),
    Course(5,
           'Computer since',
           'Marry Poppins',
           'Fundamental of computer since',
           8
    ),
    Course(3,
           'Java Backend',
           'Martin Morgan',
           'OOP, variables and loops',
           3
           ),
    Course(4,
           'Python',
           'Andrew Louder',
           'Python & Python Pro',
           5
           ),
    Course(5,
           'Databases',
           'Mark Michigan',
           'Lorem ipsum description',
           5
           )

]
class CourseRequest(BaseModel):
    id:              int
    title:           str
    trainer:         str
    description:     str
    duration_weeks:  str

@app.get('/courses')
async def read_all_courses():
    return COURSES

class Course:
    id:              int
    title:           str
    trainer:         str
    description:     str
    duration_weeks:  str

def __init__(self, id, title, trainer, description, duration_weeks):
    self.id             = id
    self.title          = title
    self.trainer        = trainer
    self.description      = description
    self.duration_weeks = duration_weeks

@app.post('/create-course')
async  def create_course(course_request: CourseRequest):
    COURSES.append(course_request)