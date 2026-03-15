from fastapi import FastAPI

app = FastAPI()

# COURSES = []

@app.get('/courses')
async def read_all_courses():
    return COURSES


class Course:
    id: int
    title: str
    trainer: str
    description: str
    duration_weeks: int

    def __init__(self, id, title, trainer, description, duration_weeks):
        self.id = id
        self.title = title
        self.trainer = trainer
        self.description = description
        self.duration_weeks = duration_weeks

COURSES = [
    Course(1,
           'Mathematics',
           'John Smith',
           'Fundamentals of math',
           4
    ),
    Course(2,
           'Computer Science',
           'Marry Poppins',
           'Fundamentals of computer science',
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


