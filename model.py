# Defines database models and schemas.

from sqlalchemy import Table, Column, Integer, String, create_engine, MetaData
from pydantic import BaseModel
from databases import Database
import os

# database connection

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./product.db") 

engine = create_engine(DATABASE_URL)
metadata = MetaData() 
database = Database(DATABASE_URL)

# Database Model for the product table:
product_table = Table(
    "product_table",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255)),
    Column("description", String(255)),
    Column("price", Integer),
    Column("image_url", String(255))
)


# Pydantic Model for creating a new product:
class ProductCreate(BaseModel):
    name: str
    description: str
    price: int
    image_url: str

class ProductReceive(BaseModel):
    id: int
    name: str
    description: str
    price: int
    image_url: str
