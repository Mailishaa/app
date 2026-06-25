
from fastapi import FastAPI
from pydantic import BaseModel
from database import create_table, add_student ,get_students,add_teacher,get_teachers,add_course,get_courses,update_student,delete_student,update_teacher,delete_teacher,update_course,delete_course

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
@app.put("/student/{id_number}")
def modify_student(id_number: int, student: Student):
    update_student(id_number, student.name, student.age, student.email, student.country, student.id_number)
    return {"message": "student updated", "student": student}
@app.delete("/student/{id_number}")
def remove_student(id_number: int):
    delete_student(id_number)
    return {"message": f"student with ID {id_number} deleted"}




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
@app.post("/teacher") 
def register_teacher(teacher:Teacher):
    add_teacher(teacher.name,teacher.course, teacher.email,teacher.tsc_number,teacher.years_of_experience) 
    return  {"message":"teacher registerd","teacher":teacher}
@app.put("/teacher/{tsc_number}")
def modify_teacher(tsc_number: int, teacher: Teacher):
    update_teacher(tsc_number, teacher.name, teacher.course, teacher.email, teacher.tsc_number, teacher.years_of_experience)
    return {"message": "teacher updated", "teacher": teacher}

@app.delete("/teacher/{tsc_number}")
def remove_teacher(tsc_number: int):
    delete_teacher(tsc_number)
    return {"message": f"teacher with TSC number {tsc_number} deleted"}




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
@app.post("/course") 
def register_course(course:Course):
    add_course(course.name,course.topics,course.is_online ,course.course_teacher,course.duration) 
    return  {"message":"course registerd","course":course}
@app.put("/course/{course_name}")
def modify_course(course_name: str, course: Course):
    update_course(course_name, course.name, course.topics, course.is_online, course.course_teacher, course.duration)
    return {"message": "course updated", "course": course}
@app.delete("/course/{course_name}")
def remove_course(course_name: str):
    delete_course(course_name)
    return {"message": f"course '{course_name}' deleted"}





   