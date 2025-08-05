from fastapi import APIRouter
from backend.database import queries

router = APIRouter()

@router.post("/sales")
def create_sale(sale: dict):
    queries.add_sale(sale)
    return {"message": "Sale recorded successfully"}
