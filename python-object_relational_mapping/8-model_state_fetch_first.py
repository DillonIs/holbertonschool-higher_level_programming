#!/usr/bin/python3
"""Print only the first object of a database"""
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

    first_result = session.query(State).order_by(State.id).first()

    if first_result:
        print(f"{first_result.id}: {first_result.name}")
    else:
        print("Nothing")

    session.close()
