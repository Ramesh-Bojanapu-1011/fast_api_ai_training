from sqlalchemy import Column, Integer, String
from core.database import Base


class Employee(Base):
    __tablename__ = "employee"
    emp_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    designation = Column(String)
    location = Column(String)
