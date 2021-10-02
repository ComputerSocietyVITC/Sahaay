import pytest
from fastapi.testclient import TestClient
from app import app


from tests.fixtures.userFix import (user, no_pass_user,
                                    unmatching_pass_user,
                                    no_fname_user, invalid_fname_user,
                                    unreg_role_user, empty_role_user, update_def_user) 

@pytest.fixture
def test_client():
    client = TestClient(app=app)
    yield client