import pytest

@pytest.fixture
def user():
    return {
        "first_name": "Mainak",
        "last_name": "Sengupta",
        "role": "mediocre person",
        "is_active": True,
        "is_admin": False,
        "password": "alPhabetG00d",
    }

@pytest.fixture
def bad_user():
    return {
        "first_name": "Mainak",
        "last_name": "Sengupta",
        "role": "mediocre person",
        "is_active": True,
        "is_admin": False,
        "password": "",
    }

