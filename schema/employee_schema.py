from pydantic import BaseModel


class Employee(BaseModel):
    full_name: str
    designation: str
    location: str


class EmployeeResponse(BaseModel):
    emp_id: int
    full_name: str
    designation: str
    location: str

    class Config:
        from_attributes = True
