import pytest
from app import schemas

import pytest
from jose import jwt
from app.config import settings


def test_root(client):
    res = client.get("/")
    print(res.json().get('message'))
    assert res.json().get('message') == "Welcome to my API -- Successfully  done CI/CD"
    assert res.status_code == 200


def test_create_user(client):
    res = client.post(
        "/users/", json={"email": "anjana@gmail.com", "password": "pass1234"})

    new_user = schemas.Userout(**res.json())
    assert new_user.email == "anjana@gmail.com"
    assert res.status_code == 201


def test_login_user(test_user, client):
    res = client.post(
        "/login", data={"username": test_user["email"], "password": test_user['password']})

    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token,
                         settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user["id"]
    assert login_res.token_type == "Bearer"
    assert res.status_code == 200


@pytest.mark.parametrize("email, password, status_code", [
    ('wrongemail@gmail.com', 'pass1234', 403),
    ("anjana@gmail.com", 'wrongpassword', 403),
    ('wrongemail@gmail.com', 'wrongpassword', 403),
    (None, 'pass1234', 422),
    ('anjanal@gmail.com', None, 422),
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post(
        "/login", data={"username": email, "password": password})

    assert res.status_code == status_code
    # assert res.json().get('detail') == 'Invalid Credentials'
