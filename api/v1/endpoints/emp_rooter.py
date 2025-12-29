from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.database import session_local
from schema.employee_schema import Employee, EmployeeResponse
from services.emp_service import employee_service

emp_rooter = APIRouter(
    prefix="/employee",
)


def get_db():
    db = session_local()
    try:
        yield db
    except Exception as e:
        raise e
    finally:
        db.close()


# insert in data
@emp_rooter.post("/add", response_model=EmployeeResponse, status_code=201)
async def add_employee(playlode: Employee, db: Session = Depends(get_db)):
    return employee_service.create_employee(
        db, playlode.full_name, playlode.designation, playlode.location
    )


@emp_rooter.get("/allemployes", response_model=list[EmployeeResponse], status_code=200)
async def get_employee(db: Session = Depends(get_db)):
    return employee_service.get_all_employee(db=db)


@emp_rooter.get(
    path="/get_an_employee",
    response_model=EmployeeResponse,
    status_code=200,
)
async def get_an_employee(employee_id: int, db: Session = Depends(get_db)):
    return employee_service.get_employee_by_id(emp_id=employee_id, db=db)


@emp_rooter.put(
    path="/update_an_employee",
    response_model=EmployeeResponse,
    status_code=200,
)
async def update_an_employee(
    employee_id: int,
    playlode: Employee,
    db: Session = Depends(get_db),
):
    return employee_service.update_employee(
        db=db,
        employee_id=employee_id,
        full_name=playlode.full_name,
        designation=playlode.designation,
        location=playlode.location,
    )


@emp_rooter.delete(path="/delete_an_employee", status_code=200)
async def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    emp_data = employee_service.delete_employee(db, employee_id)
    if not emp_data:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}
