from sqlalchemy.orm import Session
from ..models.ContactMessages import Contact
from ..schemas.contact_schema import ContactCreate
from datetime import datetime

def create_contact(db: Session, contact: ContactCreate):
    db_contact = Contact(**contact.model_dump(), SentAt=datetime.now())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def get_contacts(db: Session):
    return db.query(Contact).all()