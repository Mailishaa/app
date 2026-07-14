from fastapi import APIRouter
from schemas.course import Course
from repositories.course import(
    add_course,
    get_courses,
    update_course,
    delete_course
)
router = APIRouter(prefix="/course",tags=["courses"])


@router.get("")
def list_courses():
    courses=get_courses()
    return courses

@router.post("") 
def register_course(course:Course):
    add_course(course.name,course.topics,course.is_online ,course.course_teacher,course.duration) 
    return  {"message":"course registerd","course":course}

@router.put("/{course_name}")
def modify_course(course_name: str, course: Course):
    update_course(course_name, course.name, course.topics, course.is_online, course.course_teacher, course.duration)
    return {"message": "course updated", "course": course}

@router.delete("/{course_name}")
def remove_course(course_name: str):
    delete_course(course_name)
    return {"message": f"course '{course_name}' deleted"}





