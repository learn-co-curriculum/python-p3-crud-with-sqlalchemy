#!/usr/bin/env python3

from datetime import datetime

from sqlalchemy import (create_engine, desc,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    __table_args__ = (
        PrimaryKeyConstraint(
            'student_id',
            name='id_pk'),
        UniqueConstraint(
            'student_email',
            name='unique_email'),
        CheckConstraint(
            'student_grade BETWEEN 1 AND 12',
            name='grade_between_1_and_12'))

    Index('index_student_name', 'student_name')

    student_id = Column(Integer())
    student_name = Column(String())
    student_email = Column(String(55))
    student_grade = Column(Integer())
    student_birthday = Column(DateTime())
    student_enrolled_date = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f"Student {self.student_id}: " \
            + f"{self.student_name}, " \
            + f"Grade {self.student_grade}"

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    albert_einstein = Student(
        student_name="Albert Einstein",
        student_email="albert.einstein@zurich.edu",
        student_grade=6,
        student_birthday=datetime(
            year=1879,
            month=3,
            day=14
        ),
    )

    alan_turing = Student(
        student_name="Alan Turing",
        student_email="alan.turing@sherborne.edu",
        student_grade=11,
        student_birthday=datetime(
            year=1912,
            month=6,
            day=23
        ),
    )

    session.bulk_save_objects([albert_einstein, alan_turing])
    session.commit()

    # CRUD goes here!
