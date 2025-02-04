# Contains business logic.

from fastapi import APIRouter, HTTPException
from typing import List
from model import ProductCreate, ProductReceive
from sqlalchemy.sql import select, insert, update, delete
from model import product_table, database
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter()


# CORS middleware
def add_cors_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# API endpoints
@router.get("/", response_model=List[ProductReceive])
async def read_products():
    return await get_all_products()

@router.get("/{product_id}", response_model=ProductReceive)
async def read_product(product_id: int):
    product = await get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/", response_model=ProductCreate)
async def create_new_product(product: ProductCreate):
    return await create_product(product.dict())

@router.put("/{product_id}", response_model=ProductCreate)
async def update_existing_product(product_id: int, product: ProductCreate):
    updated = await update_product(product_id, product.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.delete("/{product_id}")
async def delete_existing_product(product_id: int):
    deleted = await delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"detail": "Product deleted successfully"}

# CRUD operations
async def get_all_products():
    query = select(product_table)
    return await database.fetch_all(query)

async def get_product_by_id(product_id: int):
    query = select(product_table).where(product_table.c.id == product_id)
    return await database.fetch_one(query)

async def create_product(product_data: dict):
    query = insert(product_table).values(product_data)
    await database.execute(query)
    return product_data

async def update_product(product_id: int, product_data: dict):
    query = update(product_table).where(product_table.c.id == product_id).values(product_data)
    result = await database.execute(query)
    return result

async def delete_product(product_id: int):
    query = delete(product_table).where(product_table.c.id == product_id)
    return await database.execute(query)
