from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from web.api.schemas.contact_schema import ContactCreate, ContactRead
from web.api.controllers.contact_controller import create_contact, get_contacts
from web.database import get_db

router = APIRouter()

@router.get("/", tags=["Validate API"])
def root():
    return {"message": "API funcionando correctamente"}

@router.post("/contacts/", response_model=ContactRead, tags=["Contacts"])
def create(contact: ContactCreate, db: Session = Depends(get_db)):
    return create_contact(db, contact)

@router.get("/contacts/", response_model=list[ContactRead], tags=["Contacts"])
def read(db: Session = Depends(get_db)):
    return get_contacts(db)