from sqlalchemy.orm import Session
from models import Memory


def save_memory(db: Session, key: str, value: str):

    obj = db.query(Memory).filter(Memory.key == key).first() # query to check if the key already exists in the database

    if obj:
        obj.value = value # if the key exists, update the value
    else:
        obj = Memory(key=key, value=value) # if the key does not exist, create a new Memory object with the provided key and value
        db.add(obj)

    db.commit() # commit the transaction to save changes to the database

    return {
        "key": key,
        "value": value,
        "status": "saved"
    }


def get_memory(db: Session, key: str):

    obj = db.query(Memory).filter(Memory.key == key).first()

    if obj:
        return {
            "key": key,
            "value": obj.value
        }

    return {
        "key": key,
        "value": None
    }