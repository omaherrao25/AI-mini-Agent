from sqlalchemy.orm import Session
from models import Memory


def save_memory(db: Session, key: str, value: str):

    obj = db.query(Memory).filter(Memory.key == key).first()

    if obj:
        obj.value = value
    else:
        obj = Memory(key=key, value=value)
        db.add(obj)

    db.commit()

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