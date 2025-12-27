from sqlalchemy.orm import Session
from models.employee import Employee


class employee_repo:

    @staticmethod
    def create_employee(db: Session, employee: Employee):
        db.add(employee)
        db.commit()
        db.refresh(employee)
        return employee

    @staticmethod
    def all_employees(db: Session):
        return db.query(Employee).all()
