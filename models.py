from sqlalchemy import Column, Integer, String
from database import Base

class Memory(Base): # SQLAlchemy model for memory storage, representing a key-value pair in the database
    __tablename__ = "memory"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True)
    value = Column(String)