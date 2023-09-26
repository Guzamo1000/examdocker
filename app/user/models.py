from app.user.database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy import Column,Integer, String, ForeignKey, Text


class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True, nullable=False)
    name=Column(String(255), nullable=False)
    number_phone=Column(String(255))
    email=Column(String(255))
    password=Column(String(255), nullable=False)
    