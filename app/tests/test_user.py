from fastapi import (status, HTTPException)
import pytest

from views.dependencies import (get_user, auth_user,
                                create_user, get_current_user,
                                delete_user, update_user)
from settings import db

@pytest.mark.usefixtures("user", "no_pass_user",
                        "no_fname_user", "unreg_role_user",
                        "empty_role_user","repeated_name_user",
                        "unusual_character_in_fname")
def test_create_user(
                        user, no_pass_user,
                        no_fname_user, unreg_role_user,
                        empty_role_user,repeated_name_user,
                        unusual_character_in_fname 
                    ):
    
    assert create_user(user).status_code == status.HTTP_201_CREATED
    assert create_user(no_pass_user).status_code == status.HTTP_400_BAD_REQUEST
    assert create_user(unreg_role_user).status_code == status.HTTP_400_BAD_REQUEST
    assert create_user(empty_role_user).status_code == status.HTTP_400_BAD_REQUEST
    assert create_user(repeated_name_user).status_code == status.HTTP_400_BAD_REQUEST
    assert create_user(unusual_character_in_fname).status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.usefixtures("user")
def test_delete_user(user):
    _id = db["users"].find_one({"first_name":user["first_name"]})

    assert delete_user(_id).status_code == status.HTTP_204_NO_CONTENT
    assert delete_user(_id).status_code == status.HTTP_404_NOT_FOUND