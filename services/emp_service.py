from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.employee import Employee
from repository.emp_repository import employee_repo


class employee_service:

    @staticmethod
    def create_employee(db: Session, full_name: str, designation: str, location: str):
        employee = Employee(
            full_name=full_name, designation=designation, location=location
        )
        return employee_repo.create_employee(db=db, employee=employee)

    @staticmethod
    def get_all_employee(db: Session):
        employees = employee_repo.all_employees(db=db)
        return employees

    @staticmethod
    def get_employee_by_id(emp_id: int, db: Session):
        return employee_repo.get_employee_by_id(db=db, employee_id=emp_id)

    @staticmethod
    def update_employee(
        full_name, designation, location, employee_id: int, db: Session
    ):
        employee = {
            "full_name": full_name,
            "designation": designation,
            "location": location,
        }
        return employee_repo.update_an_employee(
            db=db, employee_id=employee_id, employee=employee
        )

    @staticmethod
    def delete_employee(db: Session, employee_id: int):
        emp_data = employee_repo.get_employee_by_id(db=db, employee_id=employee_id)
        if not emp_data:
            raise HTTPException(status_code=404, detail="Employee not found")
        employee_repo.delete_employee(db=db, employee_id=employee_id)
        return emp_data
