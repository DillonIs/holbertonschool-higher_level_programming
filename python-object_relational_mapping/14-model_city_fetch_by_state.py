#!/usr/bin/python3
"""Print all the cities of the states from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

    result = (session.query(City, State)
              .join(State)
              .order_by(City.id)
              .all())

    for city, state in result:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
