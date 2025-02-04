#Handles API routes and endpoints with FastAPI.

from fastapi import FastAPI
from model import database, metadata, engine
from service import router as product_router
from service import add_cors_middleware

metadata.create_all(bind=engine)

#initializes the FastAPI app
app = FastAPI()

# Add CORS middleware
add_cors_middleware(app)

# Include API routes
app.include_router(product_router, prefix="/api/v1/products", tags=["Products"])

# Startup & Shutdown Events: Manages database connection lifecycle
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
