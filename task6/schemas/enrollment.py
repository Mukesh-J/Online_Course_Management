from pydantic import BaseModel

class EnrollmentResponse(BaseModel):
    enrollment_id: int
    student_id: int
    course_id: int
    status: str

    class Config:
        from_attributes = True
