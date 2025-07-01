#!/usr/bin/python3
"""Update an existing State object
object location to update id=2
Update to New Mexico"""

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

    result = (session.query(State)
              .filter(State.id == 2)
              .first())
    if result:
        result.name = "New Mexico"
        session.commit()
    else:
        print("Id not found")
    session.close()
