from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.employee import Employee


class employee_repo:

    @staticmethod
    def create_employee(db: Session, employee: Employee):
        if not employee.full_name or not employee.designation or not employee.location:
            raise HTTPException(status_code=400, detail="All fields are required")
        db.add(employee)
        db.commit()
        db.refresh(employee)
        return employee

    @staticmethod
    def all_employees(db: Session):
        return db.query(Employee).all()

    @staticmethod
    def get_employee_by_id(employee_id: int, db: Session):
        emp_data = db.query(Employee).filter(Employee.emp_id == employee_id).first()
        if not emp_data:
            raise HTTPException(status_code=404, detail="Employee not found")
        return emp_data
