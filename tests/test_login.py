import requests
import pytest

from conftest import LOGIN_ENDPOINT, VALID_CREDENTIALS

INVALID_CREDENTIALS = {
    "email": "test2@fake.com",
    "password": "wrongPassword"
}

def test_login_valid_credentials():
    response = requests.post(LOGIN_ENDPOINT, json=VALID_CREDENTIALS)
    assert response.status_code == 200, "Expected HTTP status code 200 for valid credentials"

    response_data = response.json()
    assert "user" in response_data, "'user' field is missing in the response"
    assert "token" in response_data, "'token' field is missing in the response"

    user = response_data["user"]
    assert user["email"] == VALID_CREDENTIALS["email"], "Email in the response does not match the input email"

def test_login_invalid_credentials():
    response = requests.post(LOGIN_ENDPOINT, json=INVALID_CREDENTIALS)
    assert response.status_code == 401, "Expected HTTP status code 401 for invalid credentials"

def test_login_missing_fields():
    response = requests.post(LOGIN_ENDPOINT, json={"email": "test2@fake.com"})
    assert response.status_code == 401, "Expected HTTP status code 401 for missing fields"

