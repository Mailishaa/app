from pydantic import BaseModel
class Student(BaseModel):

    name:str #type hinting (telling fast api that the name needs to be a string)
    age: int  # type hinting is enabled by the pydantic library
    email:str
    country: str
    id_number:int
#students=[]
