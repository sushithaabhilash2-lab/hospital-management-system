from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


def test_password_hashing():
    password = "Admin123"

    hashed = hash_password(password)

    assert verify_password(password, hashed)


def test_create_token():
    token = create_access_token(
        {
            "sub": "admin@gmail.com",
            "role": "ADMIN"
        }
    )

    assert token is not None
    assert isinstance(token, str)