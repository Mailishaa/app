from fastapi import APIRouter
from schemas.teacher import Teacher
from repositories.teacher import(
    add_teacher,
    get_teachers,
    update_teacher,
    delete_teacher
)
router = APIRouter(prefix="/teacher",tags=["teachers"])


@router.get("")
def list_teachers():
    teachers= get_teachers ()
    return [dict(teacher) for teacher in teachers] 

@router.post("") 
def register_teacher(teacher:Teacher):
    add_teacher(teacher.name,teacher.course, teacher.email,teacher.tsc_number,teacher.years_of_experience) 
    return  {"message":"teacher registerd","teacher":teacher}

@router.put("/{tsc_number}")
def modify_teacher(tsc_number: int, teacher: Teacher):
    update_teacher(tsc_number, teacher.name, teacher.course, teacher.email, teacher.tsc_number, teacher.years_of_experience)
    return {"message": "teacher updated", "teacher": teacher}

@router.delete("/teacher/{tsc_number}")
def remove_teacher(tsc_number: int):
    delete_teacher(tsc_number)
    return {"message": f"teacher with TSC number {tsc_number} deleted"}
