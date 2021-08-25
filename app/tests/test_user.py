from fastapi import (status, HTTPException)
import pytest

from views.dependencies import (get_user, auth_user,
                                create_user, get_current_user)

@pytest.mark.usefixtures("user", "bad_user")
def test_create_user(user, bad_user):
    
    assert create_user(user).status_code == status.HTTP_201_CREATED
    assert create_user(bad_user).status_code == status.HTTP_201_CREATED
