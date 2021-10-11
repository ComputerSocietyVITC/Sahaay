import pytest


@pytest.mark.usefixtures(
    "user",
    "no_pass_user",
    "unmatching_pass_user",
    "no_fname_user",
    "invalid_fname_user",
    "unreg_role_user",
    "empty_role_user",
)
def test_create_user(
    user,
    no_pass_user,
    unmatching_pass_user,
    no_fname_user,
    invalid_fname_user,
    unreg_role_user,
    empty_role_user,
    test_client,
):

    url = "/user"

    _data = [
        user,
        no_pass_user,
        unmatching_pass_user,
        no_fname_user,
        invalid_fname_user,
        unreg_role_user,
        empty_role_user,
    ]
    _response = [201, 422, 422, 422, 422, 422, 422]

    for i in range(len(_data)):
        response = test_client.post(url, json=_data[i])
        assert response.status_code == _response[i]


@pytest.mark.usefixtures("update_def_user", "user")
def test_update_user(update_def_user, user, test_client):
    url = "/user/update"
    response = test_client.patch(
        url, params={"email": user["email"]}, json=update_def_user
    )
    assert response.status_code == 200
