from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQL_SERVER_URL = "mssql+pyodbc://localhost\\SQLEXPRESS/Euexia?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(SQL_SERVER_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()