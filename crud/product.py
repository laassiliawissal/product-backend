from sqlalchemy.sql import select, insert, update, delete
from models.product import product_table
from core.database import database

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
