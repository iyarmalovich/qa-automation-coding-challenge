import pytest
import requests
from config.settings import BASE_URL, USERNAME, PASSWORD

LOGIN_ENDPOINT = f"{BASE_URL}/users/login"

VALID_CREDENTIALS = {
    "email": f"{USERNAME}",
    "password": f"{PASSWORD}"
}


# Define the auth_token fixture
@pytest.fixture
def auth_token():

    # Send login request and get the token
    response = requests.post(LOGIN_ENDPOINT, json=VALID_CREDENTIALS)

    # Assert the login was successful (status code 200)
    assert response.status_code == 200, f"Login failed: {response.text}"

    # Extract the token from the response
    token = response.json().get('token')

    # Return the token for use in the test
    return token