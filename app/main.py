
from fastapi import FastAPI
from models import create_table
from routers import student, teacher, course

app= FastAPI()    # instance 
create_table()

app.include_router(student.router)
app.include_router(teacher.router)
app.include_router(course.router)































   