from pydantic import BaseModel,Field
from typing import Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls,v):
        if not ObjectId.is_valid(v):
            raise ValueError("invalid objectid")
        return str(v)
    
class Movement(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    description: str
    amount: float
    saldo: float
    date: str

class Task(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    title: str
    description: Optional[str]=None
    completed: bool = False

    class Config:
        orm_mode = True
        allow_population_by_field_name=True
        json_encoders = {ObjectId: str}

class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: str
        }


