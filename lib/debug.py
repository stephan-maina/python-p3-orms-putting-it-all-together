#!/usr/bin/env python3

# debug.py
from dog import Dog, Session, Base

# Create the database tables
Base.metadata.create_all()

# Create a session
session = Session()

# Add sample dog records
dog1 = Dog(name='Buddy', breed='Golden Retriever')
dog2 = Dog(name='Max', breed='Labrador Retriever')
session.add(dog1)
session.add(dog2)
session.commit()
