import pytest
import requests
from config.settings import BASE_URL, USERNAME, PASSWORD


# Define the auth_token fixture
@pytest.fixture
def auth_token():
    # Define the login URL based on the base URL from config
    url = f'{BASE_URL}/login'
    data = {
        'username': USERNAME,
        'password': PASSWORD
    }

    # Send login request and get the token
    response = requests.post(url, data=data)

    # Assert the login was successful (status code 200)
    assert response.status_code == 200, f"Login failed: {response.text}"

    # Extract the token from the response
    token = response.json().get('token')

    # Return the token for use in the test
    return token