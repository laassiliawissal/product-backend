
# Backend API for Product Management
This is a FastAPI-based backend API designed to *manage products*. It provides CRUD operations for product management and includes a well-structured architecture that separates concerns for maintainability and scalability.


## Prepare the Environment

Before running the application, ensure you have Python installed and set up a virtual environment. Then, install the necessary dependencies:

1. Create and Activate a Virtual Environment
```bash
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate on macOS
```
2. Install Required Dependencies
```bash
pip install fastapi uvicorn sqlalchemy databases pydantic
```

3. Run the Application

```bash
uvicorn main:app --reload
```
## Code anatomy:

### main.py:
it's the main entry point to the application. 
- it initializes the FastApi app, 
- includes the routes ( Includes product routes under /api/v1/products), 
- sets up the database, (Startup & Shutdown Events: Manages database connection lifecycle) 
- configure middleware (Ensures frontend communication is allowed).


### The Schema:(schemas/product.py)
Defines the structure of API request and response bodies using Pydantic. Ensures type validation and consistency.

it's the pydantic schema that is used to make sure that the api response is respecting the disired schema that we define, it Ensures type validation and consistency. 
for the product.py schema, the schema is used to make sure that  
    name: str
    description: str
    price: int
    image_url: str
are provided in the correct types.

###  The model:(models/product.py)
Defines the structure of the product_table in the database using SQLAlchemy.

### Core (core/database.py)
Defines database connectivity settings using *SQLAlchemy* and *Databases* library.

### CRUD
Implements database operations for product management (Create, Read, Update, Delete).

### Api
Defines API endpoints using FastAPI's APIRouter, linking them to CRUD operations.

### The moddleware: (middlewares/cors.py)
Configures CORS (Cross-Origin Resource Sharing) to allow frontend interactions


### Summary

This FastAPI backend follows a modular architecture:

- Main: Initializes the app, middleware, and database lifecycle.
- Schemas: Defines request/response validation.
- Models: Defines database structure.
- Database: Manages database connections.
- CRUD: Implements business logic for data operations.
- API: Exposes endpoints using FastAPI.
- Middleware: Configures security and communication policies.

This design promotes clean separation of concerns, making the API scalable and maintainable.
