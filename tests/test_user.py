import requests

from conftest import USER_ENDPOINT, VALID_CREDENTIALS
from logger import logger
from tests.constants import INVALID_CREDENTIALS


def test_login_valid_credentials():
    response = requests.post(USER_ENDPOINT + "/login", json=VALID_CREDENTIALS)
    assert response.status_code == 200

    response_data = response.json()
    assert "user" in response_data
    assert "token" in response_data

    user = response_data["user"]
    assert user["email"] == VALID_CREDENTIALS["email"]

def test_login_invalid_credentials():
    response = requests.post(USER_ENDPOINT + "/login", json=INVALID_CREDENTIALS)
    assert response.status_code == 401

def test_login_missing_fields():
    response = requests.post(USER_ENDPOINT + "/login", json={"email": "test2@fake.com"})
    assert response.status_code == 401


def test_create_user(auth_token, user_data):
    logger.info("Sending POST request to create a new user")
    logger.info(f"Request body: {user_data}")

    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(USER_ENDPOINT, json=user_data, headers=headers)

    logger.info(f"Received response: status = {response.status_code}, body = {response.text}")

    assert response.status_code == 201

    response_data = response.json()
    assert "user" in response_data
    assert "token" in response_data

    user_data = response_data["user"]
    assert user_data["firstName"] == user_data["firstName"]
    assert user_data["lastName"] == user_data["lastName"]
    assert user_data["email"] == user_data["email"]

    logger.info("User created successfully with data: %s", user_data)
    logger.info("Received token: %s", response_data['token'])
