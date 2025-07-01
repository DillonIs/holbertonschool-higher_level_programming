#!/usr/bin/python3
"""Add a new State object to a database
State object to be added Louisiana"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost/{database}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = State(name="Louisiana")
    session.add(result)
    session.commit()

    if result:
        print(f"{result.id}")
    else:
        print("Not found")

    session.close()
