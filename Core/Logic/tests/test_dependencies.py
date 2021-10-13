from views.dependencies import hash_password, verify_password


def test_password_verification():
    plain_password = "test_password"
    hashed_password = hash_password(plain_password)
    incorrect_hash = hash_password("fail_test")

    assert verify_password(plain_password, hashed_password) == True
    assert verify_password("fail_test", hashed_password) == False
    assert verify_password(plain_password, incorrect_hash) == False
