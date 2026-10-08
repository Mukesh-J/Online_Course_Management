from pydantic import BaseModel, Field
from typing import Optional

class CourseCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = None
    category: str = Field(min_length=1, max_length=100)
    price: float = Field(ge=0)

class CourseUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = Field(default=None, ge=0)

class InstructorResponse(BaseModel):
    user_id: int
    name: str

    class Config:
        from_attributes = True

class CourseResponse(BaseModel):
    course_id: int
    title: str
    description: Optional[str]
    category: str
    price: float
    instructor_id: int
    is_active: bool
    instructor: InstructorResponse

    class Config:
        from_attributes = True
