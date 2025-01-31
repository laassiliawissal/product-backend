from sqlalchemy import create_engine, MetaData
from databases import Database
from config import Config


engine = create_engine(Config.DATABASE_URL) # Creates a connection engine for the specified database. This engine is used for executing raw SQL queries synchronously.
metadata = MetaData() # An object that stores information about the database schema. It keeps track of all defined tables and relationships.
database = Database(Config.DATABASE_URL) # Initializes an asynchronous database connection. This allows us to perform database operations asynchronously with FastAPI.


# create_engine: This function initializes a database connection engine, which *allows SQLAlchemy to communicate with the database*
# MetaData: This is a container that holds schema definitions (like tables, columns, and constraints) for SQLAlchemy. 
# Database: This class provides async methods for executing SQL queries and transactions.
# os module: Used to interact with the operating system, such as reading environment variables.

