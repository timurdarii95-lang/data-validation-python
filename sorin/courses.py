from fastapi import FastAPI

app = FastAPI()

COURSES = []

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
