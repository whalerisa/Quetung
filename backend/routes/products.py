from fastapi import APIRouter
from backend.database import queries

router = APIRouter()

@router.get("/products")
def read_products():
    return queries.get_products()
