from fastapi import APIRouter
from api.v1.endpoints.emp_rooter import emp_rooter

api_router = APIRouter()
api_router.include_router(emp_rooter, tags=["employee root"])
