from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from models import Base

engine = create_engine('postgresql://postgres:postgres@localhost/postgres')
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base.metadata.create_all(engine)
Base.metadata.bind = engine
