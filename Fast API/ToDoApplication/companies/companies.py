from fastapi import FastAPI , APIRouter


router = APIRouter()

@router.get("/")
async def get_company():
    return {"company_name":"Example company,LLS"}

@router.get("/employees")
async def number_of_employees():
    return 100;

