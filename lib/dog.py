# dog.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)

engine = create_engine('sqlite:///dogs.db')
Session = sessionmaker(bind=engine)
