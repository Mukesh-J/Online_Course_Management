from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database.connection import get_db
from database.models import User, Course
from schemas.course import CourseCreate, CourseUpdate, CourseResponse
from dependencies.auth import get_current_user, require_roles

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.post("", response_model=CourseResponse, status_code=201)
def create_course(data: CourseCreate, db: Session = Depends(get_db),
                  current_user: User = Depends(require_roles("admin", "instructor"))):
    course = Course(
        title=data.title, description=data.description, category=data.category,
        price=data.price, instructor_id=current_user.user_id, is_active=True
    )
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

@router.get("", response_model=list[CourseResponse])
def get_courses(
    category: str | None = None,
    is_active: bool | None = True,
    min_price: float | None = Query(default=None, ge=0),
    max_price: float | None = Query(default=None, ge=0),
    search: str | None = None,
    sort_by: str = "course_id",
    sort_order: str = "asc",
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    query = db.query(Course)
    if category:
        query = query.filter(Course.category == category)
    if is_active is not None:
        query = query.filter(Course.is_active == is_active)
    if min_price is not None:
        query = query.filter(Course.price >= min_price)
    if max_price is not None:
        query = query.filter(Course.price <= max_price)
    if search:
        query = query.filter(Course.title.ilike(f"%{search}%"))

    if sort_by == "price":
        column = Course.price
    elif sort_by == "title":
        column = Course.title
    else:
        column = Course.course_id

    query = query.order_by(column.desc() if sort_order.lower() == "desc" else column.asc())
    return query.offset((page - 1) * limit).limit(limit).all()

@router.get("/{course_id}", response_model=CourseResponse)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.course_id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.put("/{course_id}", response_model=CourseResponse)
def update_course(course_id: int, data: CourseUpdate, db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    course = db.query(Course).filter(Course.course_id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    if current_user.role != "admin" and course.instructor_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="You can modify only your own course")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(course, key, value)
    db.commit()
    db.refresh(course)
    return course

@router.patch("/{course_id}", response_model=CourseResponse)
def patch_course(course_id: int, data: CourseUpdate, db: Session = Depends(get_db),
                 current_user: User = Depends(get_current_user)):
    return update_course(course_id, data, db, current_user)

@router.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db),
                  current_user: User = Depends(require_roles("admin", "instructor"))):
    course = db.query(Course).filter(Course.course_id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    if current_user.role != "admin" and course.instructor_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="You can delete only your own course")
    course.is_active = False
    db.commit()
    return {"message": "Course deactivated successfully"}
