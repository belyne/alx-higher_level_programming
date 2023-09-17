#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa.

This script uses SQLAlchemy to connect to a MySQL server and retrieve a list of
states from the database hbtn_0e_0_usa. It specifically filters for states with
names starting with the letter 'N' and prints the results to the console.

Usage:
    ./1-filter_states.py <username> <password> <database_name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """Main function"""

    # Create an engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a session class
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states with names starting with 'N'
    states = session.query(State).filter(State.name.like('N%')).order_by(State.id).all()

    # Print the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
