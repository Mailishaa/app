
from fastapi import FastAPI
from pydantic import BaseModel
from database import create_table, add_student ,get_students,add_teacher,get_teachers,add_course,get_courses

app= FastAPI()    # instance 
class Student(BaseModel):
    name:str #type hinting (telling fast api that the name needs to be a string)
    age: int  # type hinting is enabled by the pydantic library
    email:str
    country: str
    id_number:int
#students=[]
create_table()


@app.get("/")    #a decoretor for creating routes
def home():
    return{"message":"Welcome to my first server"}
@app.get("/students")
def list_students():
    students=get_students ()
    return [dict(student) for student in students]
@app.post("/student") # this a decorator for creating data therfore we use POST
def register_student(student:Student):# this  is an object student that should look like the class Student
    add_student(student.name,student.age, student.email,student.country,student.id_number)#student.append(student) 
    return  {"message":"student registerd","student":student}

class Teacher(BaseModel):
    name : str
    course:str
    tsc_number : int
    email: str
    years_of_experience: int
@app.get("/teachers")
def list_teachers():
    teachers= get_teachers ()
    return [dict(teacher) for teacher in teachers] 
@app.post("/teacher") # this a decorator for creating data therfore we use POST
def register_teacher(teacher:Teacher):# this  is an object student that should look like the class Student
    add_teacher(teacher.name,teacher.course, teacher.email,teacher.tsc_number,teacher.years_of_experience)#student.append(student) 
    return  {"message":"teacher registerd","teacher":teacher}


class Course (BaseModel):
    name:str
    topics:int 
    is_online:bool
    course_teacher:str
    duration:str
@app.get("/courses")
def list_courses():
    courses=get_courses()
    return courses
@app.post("/course") # this a decorator for creating data therfore we use POST
def register_course(course:Course):# this  is an object student that should look like the class Student
    add_course(course.name,course.topics,course.is_online ,course.course_teacher,course.duration)#student.append(student) 
    return  {"message":"course registerd","course":course}


