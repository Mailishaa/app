from pydantic import BaseModel
class Teacher(BaseModel):
    name : str
    course:str
    tsc_number : int
    email: str
    years_of_experience: int