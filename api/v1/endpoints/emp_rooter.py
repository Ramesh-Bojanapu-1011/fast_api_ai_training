from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session


from schema.employee_schema import Employee, EmployeeResponse
from services.emp_service import employee_service
from core.database import session_local


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
