from fastapi import FastAPI

app = FastAPI()

COURSES = []

@app.get('/courses')
async def read_all_courses():
    return COURSES
