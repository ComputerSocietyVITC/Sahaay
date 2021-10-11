import pytest


@pytest.fixture
def user():
    return {
        "first_name": "Mainak",
        "last_name": "Sengupta",
        "role": "simple mortal",
        "email": "test@user.com",
        "is_active": False,
        "is_admin": False,
        "created_at": "datetime",
        "last_login": "datetime",
        "password": "alPhabetG00d",
        "password_reverification": "alPhabetG00d",
    }


@pytest.fixture
def no_pass_user():
    return {
        "first_name": "Mainak",
        "last_name": "Sengupta",
        "role": "simple mortal",
        "email": "test@user.com",
        "is_active": False,
        "is_admin": False,
        "created_at": "datetime",
        "last_login": "datetime",
        "password": "",
        "password_reverification": "alPhabetG00d",
    }


@pytest.fixture
def unmatching_pass_user():
    return {
        "first_name": "Mainak",
        "last_name": "Sengupta",
        "role": "simple mortal",
        "email": "test@user.com",
        "is_active": False,
        "is_admin": False,
        "created_at": "datetime",
        "last_login": "datetime",
        "password": "alPhabetG00d",
        "password_reverification": "alPhabetgood",
    }


@pytest.fixture
def no_fname_user():
    return {
        "first_name": "",
        "last_name": "Sengupta",
        "role": "simple mortal",
        "email": "test@user.com",
        "is_active": False,
        "is_admin": False,
        "created_at": "datetime",
        "last_login": "datetime",
        "password": "alPhabetG00d",
        "password_reverification": "alPhabetG00d",
    }


@pytest.fixture
def invalid_fname_user():
    return {
        "first_name": "Mainak  ",
        "last_name": "Sengupta",
        "role": "simple mortal",
        "email": "test@user.com",
        "is_active": False,
        "is_admin": False,
        "created_at": "datetime",
        "last_login": "datetime",
        "password": "alPhabetG00d",
        "password_reverification": "alPhabetG00d",
    }


@pytest.fixture
def unreg_role_user():
    return {
        "first_name": "Mainak  ",
        "last_name": "Sengupta",
        "role": "mediocre mortal",
        "email": "test@user.com",
        "is_active": False,
        "is_admin": False,
        "created_at": "datetime",
        "last_login": "datetime",
        "password": "alPhabetG00d",
        "password_reverification": "alPhabetG00d",
    }


@pytest.fixture
def empty_role_user():
    return {
        "first_name": "Mainak  ",
        "last_name": "Sengupta",
        "role": "",
        "email": "test@user.com",
        "is_active": False,
        "is_admin": False,
        "created_at": "datetime",
        "last_login": "datetime",
        "password": "alPhabetG00d",
        "password_reverification": "alPhabetG00d",
    }


@pytest.fixture
def update_def_user():
    return {
        "first_name": "Manak",
    }
