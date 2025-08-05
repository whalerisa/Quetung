from fastapi import APIRouter
from backend.database import queries

router = APIRouter()

@router.get("/customers")
def read_customers():
    return queries.get_customers()

@router.post("/customers")
def create_customer(customer: dict):
    queries.add_customer(customer)
    return {"message": "Customer added successfully"}
