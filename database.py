from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:root@localhost:5432/agentdb" # pointing to local Postgres instance

engine = create_engine(DATABASE_URL) # create SQLAlchemy engine

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
) # create session factory for database interactions

Base = declarative_base() # base class for SQLAlchemy models, used for defining database tables and ORM models