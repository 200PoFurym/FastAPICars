from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class CategoryCars(Base):
    __tablename__ = 'category'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    datetime = Column(DateTime)

class Cars(Base):
    __tablename__ = 'cars'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    year = Column(Integer)
    quantity = Column(Integer, nullable=False)
    e_power = Column(String, nullable=False)
    type = Column(String, nullable=False)
    datetime = Column(DateTime)
