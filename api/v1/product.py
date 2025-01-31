from fastapi import APIRouter, HTTPException
from typing import List
from schemas.product import ProductCreate
from crud.product import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product,
)

router = APIRouter()

@router.get("/", response_model=List[ProductCreate])
async def read_products():
    return await get_all_products()

@router.get("/{product_id}", response_model=ProductCreate)
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
