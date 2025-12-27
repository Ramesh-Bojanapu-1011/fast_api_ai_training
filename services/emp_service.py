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
