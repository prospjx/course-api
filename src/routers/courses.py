from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.schemas import CourseResponse
from src.models import Course

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)

@router.get("", response_model=List[CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    """Retrieves a list of all courses available in the catalog."""
    return db.query(Course).all()

@router.get("/{course_id}", response_model=CourseResponse)
def get_course_details(course_id: str, db: Session = Depends(get_db)):
    """Get detailed information about a specific course."""
    course = db.query(Course).filter(Course.course_id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
