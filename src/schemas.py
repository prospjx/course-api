from pydantic import BaseModel
from typing import List, Optional

class TimeslotBase(BaseModel):
    day: str
    start_time: str
    end_time: str
    location: Optional[str] = None

class TimeslotResponse(TimeslotBase):
    class Config:
        from_attributes = True

class CourseBase(BaseModel):
    course_id: str
    title: str
    credits: int
    description: Optional[str] = None
    prerequisites: List[str] = []

class CourseResponse(CourseBase):
    timeslots: List[TimeslotResponse] = []
    
    class Config:
        from_attributes = True
