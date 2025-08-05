from fastapi import FastAPI
from backend.routes import customer, products, sales

app = FastAPI()

app.include_router(customer.router)
app.include_router(products.router)
app.include_router(sales.router)
