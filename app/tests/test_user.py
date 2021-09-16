from fastapi.testclient import TestClient

from app import app

import pytest

client = TestClient(app)

@pytest.mark.usefixtures("user", "no_pass_user",
                        "unmatching_pass_user", "no_fname_user",
                        "invalid_fname_user","unreg_role_user",
                        "empty_role_user")
def test_create_user(user,no_pass_user,
                    unmatching_pass_user,
                    no_fname_user, invalid_fname_user,
                    unreg_role_user, empty_role_user):
    
    response = client.post("/user",json = user)
    assert response.status_code == 201
    
    response = client.post("/user",json = no_pass_user)
    assert response.status_code == 422
    
    response = client.post("/user",json = unmatching_pass_user)
    assert response.status_code == 422
    
    response = client.post("/user",json = no_fname_user)
    assert response.status_code == 422
    
    response = client.post("/user",json = invalid_fname_user)
    assert response.status_code == 422
    
    response = client.post("/user",json = unreg_role_user)
    assert response.status_code == 422
    
    response = client.post("/user",json = empty_role_user)
    assert response.status_code == 422