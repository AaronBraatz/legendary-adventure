"""Configurations which get shared over multiple tests"""
import pytest


@pytest.fixture(scope='session')  # "session" if tests shall share (in this case) one connection
def db_conn():
    """
    Setup for DB connection.
    :return: DB connection
    """
    db = ...
    url = ...

    with db.connect(url) as conn:
        yield conn  # yield if after som tare down procedure is needed, otherwise return
