# Database Model for the product table:

from sqlalchemy import Table, Column, Integer, String
from core.database import metadata

product_table = Table(
    "product_table",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255)),
    Column("description", String(255)),
    Column("price", Integer),
    Column("image_url", String(255))
)