from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


database_uri="mysql+pymysql://root:password@mysql:3306/examdockerfile"
engine=create_engine(database_uri)

SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try: 
        yield db
    finally:
        db.close()