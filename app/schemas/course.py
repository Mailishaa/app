from pydantic import BaseModel
class Course (BaseModel):
    name:str
    topics:int 
    is_online:bool
    course_teacher:str
    duration:str