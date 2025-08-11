from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Contact(Base):
    __tablename__ = "ContactMessages"
    Id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, index=True)
    Email = Column(String, index=True)
    Message = Column(String)
    SentAt = Column(DateTime, default=datetime.now)