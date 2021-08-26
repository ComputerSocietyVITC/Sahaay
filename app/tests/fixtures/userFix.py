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
def no_pass_user():
    return {
        "first_name": "Mainak",
        "last_name": "Sengupta",
        "role": "mediocre person",
        "is_active": True,
        "is_admin": False,
        "password": "",
    }

@pytest.fixture
def no_fname_user():
    return {
        "first_name": "",
        "last_name": "Sengupta",
        "role": "mediocre person",
        "is_active": True,
        "is_admin": False,
        "password": "passtobehash",
    }

@pytest.fixture
def unreg_role_user():
    return {
        "first_name": "Mainak",
        "last_name": "Sengupta",
        "role": "programmer",
        "is_active": True,
        "is_admin": False,
        "password": "passtobehash",
    }

@pytest.fixture
def empty_role_user():
    return {
        "first_name": "Mainak",
        "last_name": "Sengupta",
        "role": " ",
        "is_active": True,
        "is_admin": False,
        "password": "passtobehash",
    }

@pytest.fixture
def unusual_character_in_fname():
    return {
        "first_name": "M@!nak",
        "last_name": "Sengupta",
        "role": "mediocre person",
        "is_active": True,
        "is_admin": False,
        "password": "passtobehash",
    }

@pytest.fixture
def repeated_name_user():
    return {
        "first_name": "Mainak",
        "last_name": "Sengupta",
        "role": "mediocre person",
        "is_active": True,
        "is_admin": False,
        "password": "passtobehash",
    }