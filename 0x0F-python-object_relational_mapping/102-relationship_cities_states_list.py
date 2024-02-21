#!/usr/bin/python3
""" A module that  prints the State object with the
name passed as argument from the DB
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    st = session.query(State).join(City).order_by(City.id).all()
    for state in st:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
