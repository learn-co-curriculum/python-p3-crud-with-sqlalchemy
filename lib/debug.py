#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_sandbox import Base, Student

if __name__ == '__main__':

    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    
    import ipdb; ipdb.set_trace()
