from email.policy import default
from typing import Optional

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field


app = FastAPI()

class Course:
    id:              int
    title:           str
    trainer:         str
    description:     str
    duration_weeks:  int

    def __init__(self, id, title, trainer, description, duration_weeks):
        self.id = id
        self.title = title
        self.trainer = trainer
        self.description = description
        self.duration_weeks = duration_weeks

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
    id:              Optional [int] = Field(description='ID is not needed to be created', default=None)
    title:           str = Field(description='ciuvac minimum 3',min_length=3)
    trainer:         str = Field(min_length=1)
    description:     str = Field(min_length=1, max_length=100)
    duration_weeks:  int = Field(gt=0,lt=6)

def find_course_id(course: Course):
    if len(COURSES) > 0:
        course.id = COURSES[-1].id + 1
    else:
        course.id = 1

    return course

@app.get('/courses')
async def read_all_courses():
    return COURSES





@app.post('/create-course')
async def create_course(course_request: CourseRequest):
    new_course = Course(**course_request.model_dump())
    print(type(new_course))
    COURSES.append(new_course)

