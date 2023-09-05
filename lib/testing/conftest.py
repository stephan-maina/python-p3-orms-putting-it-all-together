#!/usr/bin/env python3
# conftest.py
import pytest
from dog import engine, Base

@pytest.fixture(scope="module")
def setup_and_teardown():
    # Setup
    Base.metadata.create_all(bind=engine)
    yield
    # Teardown
    Base.metadata.drop_all(bind=engine)
