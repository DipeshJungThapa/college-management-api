from fastapi import APIRouter, HTTPException, Depends
from .auth import get_current_user

router = APIRouter()

students = {}
next_id = 1

@router.get("/students")
def get_all_students(user: str = Depends(get_current_user)):
    return list(students.values())

@router.get("/students/{student_id}")
def get_student(student_id: int, user: str = Depends(get_current_user)):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]

@router.post("/students")
def add_student(student: dict, user: str = Depends(get_current_user)):
    global next_id
    student["id"] = next_id
    students[next_id] = student
    next_id += 1
    return student

@router.put("/students/{student_id}")
def update_student(student_id: int, new_data: dict, user: str = Depends(get_current_user)):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    new_data["id"] = student_id
    students[student_id] = new_data
    return new_data

@router.delete("/students/{student_id}")
def delete_student(student_id: int, user: str = Depends(get_current_user)):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    del students[student_id]
    return {"message": "Student deleted"}
