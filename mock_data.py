from faker import Faker
from models.product import product_table
from sqlalchemy import create_engine
from core.database import DATABASE_URL, metadata, engine
from databases import Database

fake = Faker()

# Initialize the database connection
db = Database(DATABASE_URL)

# Create the tables if they do not exist
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)

async def generate_mock_data(num_records: int):
    await db.connect()

    for _ in range(num_records):
        name = fake.word()
        description = fake.sentence()
        price = fake.random_int(min=1, max=1000)
        image_url = fake.image_url()

        # Insert mock data into the 'product' table
        query = product_table.insert().values(
            name=name,
            description=description,
            price=price,
            image_url=image_url
        )
        await db.execute(query)

    await db.disconnect()

# Call this function to generate mock data
# Example: Generate 10 mock products
if __name__ == "__main__":
    import asyncio
    asyncio.run(generate_mock_data(20))
