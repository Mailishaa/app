from fastapi import APIRouter
from schemas.student import Student
from repositories.student import(
    add_student,
    get_students,
    update_student,
    delete_student
)
router = APIRouter(prefix="/students",tags=["students"])

@router.post("")
def register_student(student:Student):
    add_student(student.name,student.age, student.email,student.country,student.id_number)
    return  {"message":"student registerd","student":student}

@router.get("")
def list_students():
    students= get_students ()
    return [dict(student) for student in students] 

@router.put("/{id_number}")
def modify_student(id_number: int, student: Student):
    update_student(id_number, student.name, student.age, student.email, student.country, student.id_number)
    return {"message": "student updated", "student": student}  

@router.delete("/{id_number}")
def remove_student(id_number: int):
    delete_student(id_number)
    return {"message": f"student with ID {id_number} deleted"} 

