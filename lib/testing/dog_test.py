# dog_test.py
import pytest
from dog import Dog, Session

@pytest.fixture
def setup_and_teardown():
    # Setup
    session = Session()
    yield session
    # Teardown
    session.close()

def test_create_python_objects(setup_and_teardown):
    session = setup_and_teardown

    # Query the database and create Python objects
    dogs = session.query(Dog).all()
    assert len(dogs) == 2
    assert dogs[0].name == 'Buddy'

def test_create_sql_records(setup_and_teardown):
    session = setup_and_teardown

    # Create Python objects and save them to the database
    dog3 = Dog(name='Lucy', breed='Beagle')
    session.add(dog3)
    session.commit()

    # Query the database to verify the insertion
    dog_from_db = session.query(Dog).filter_by(name='Lucy').first()
    assert dog_from_db is not None
