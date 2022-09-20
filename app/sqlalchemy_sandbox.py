#!/usr/bin/env python3

from datetime import datetime

from sqlalchemy import create_engine, desc, func, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer(), primary_key=True)
    student_name = Column(String())

if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
