from email.policy import default
from typing import Optional

from fastapi import FastAPI, Body, HTTPException, Path, Query

from pydantic import BaseModel, Field
from starlette import status


app = FastAPI()

class Course:
    id:              int
    title:           str
    trainer:         str
    description:     str
    duration_weeks:  int
    start_year:      int

    def __init__(self, id, title, trainer, description, duration_weeks, start_year):
        self.id = id
        self.title = title
        self.trainer = trainer
        self.description = description
        self.duration_weeks = duration_weeks
        self.start_year = start_year

COURSES = [
    Course(1,
           'Matematics',
           'Jhon Smith',
           'Fundamentals of maths',
           4,
           2020

    ),
    Course(5,
           'Computer since',
           'Marry Poppins',
           'Fundamental of computer since',
           8,
           2019
    ),
    Course(3,
           'Java Backend',
           'Martin Morgan',
           'OOP, variables and loops',
           3,
           2015
           ),
    Course(4,
           'Python',
           'Andrew Louder',
           'Python & Python Pro',
           5,
           2010
           ),
    Course(7,
           'Databases',
           'Mark Michigan',
           'Lorem ipsum description',
           5,
           2023


           )

]
class CourseRequest(BaseModel):
    id:              Optional [int] = Field(description='ID is not needed to be created', default=None)
    title:           str = Field(description='ciuvac minimum 3',min_length=3)
    trainer:         str = Field(min_length=1)
    description:     str = Field(min_length=1, max_length=100)
    duration_weeks:  int = Field(gt=0,lt=6)
    start_year: int = Field(gt= 2020, lt=2031)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Titel of a new car",
                "trainer": "Martin Morgan",
                "description": "A new description of a course",
                "duration_weeks":4,
                "start_year": 2026

            }
        }
    }

def find_course_id(course: Course):
    if len(COURSES) > 0:
        course.id = COURSES[-1].id + 1
    else:
        course.id = 1

    return course

@app.get('/courses', status_code=status.HTTP_200_OK)
async def read_all_courses():
    return COURSES

@app.get('/courses/{course_id}')
async  def read_course(course_id: int = Path(gt=0)):
    for course in COURSES:
        if course.id == course_id:
            return course
    raise HTTPException(status_code=404, detail='nihuia')

@app.get('/courses/', status_code=status.HTTP_200_OK)
async  def read_course_by_duration(course_duration: int = Query(gt=0, lt=6)):
    courses_to_return = []
    for course in COURSES:
         if course.duration_weeks == course_duration:
            courses_to_return.append(course)
    return courses_to_return

@app.post('/create-course', status_code=status.HTTP_201_CREATED)
async def create_course(course_request: CourseRequest):
    new_course = Course(**course_request.model_dump())
    print(type(new_course))
    COURSES.append(new_course)

@app.put('/courses/update_course', status_code=status.HTTP_204_NO_CONTENT)
async def update_course(course: CourseRequest):
    course_changed =False
    for i in range (len(COURSES)):
        if COURSES[i].id == course.id:
            COURSES[i] = course
            course_changed = True
            if not course_changed:
                raise  HTTPException(status_code=404, detail='nihuia')

@app.delete('/courses/{course_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: int = Path(gt=0)):
    course_changed = False
    for i in range(len(COURSES)):
        if COURSES[i].id == course_id:
            COURSES.pop(i)
            break
            course_changed = True
    if not course_changed:
         raise HTTPException(status_code=404, detail='nihuia')

@app.get('/courses/publish/', status_code=status.HTTP_200_OK)
async def read_course_by_start_year(start_year: int = Query(gt=2020, lt=2031)):
    course_to_return = []
    for course in COURSES:
        if course.start_year == start_year:
            course_to_return.append(course)
    return course_to_return