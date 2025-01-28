import uuid
import pytest
import requests
from playwright.sync_api import sync_playwright
from tests.constants import USER_ENDPOINT, VALID_CREDENTIALS

# Define the auth_token fixture
@pytest.fixture(scope="session")
def auth_token():

    # Send login request and get the token
    response = requests.post(USER_ENDPOINT + "/login", json=VALID_CREDENTIALS)

    # Assert the login was successful (status code 200)
    assert response.status_code == 200, f"Login failed: {response.text}"

    # Extract the token from the response
    token = response.json().get('token')

    # Return the token for use in the test
    return token

@pytest.fixture(scope="session")
def browser():
    """Fixture to initialize and close the browser."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)  # Set to True for headless mode
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def user_data():
    return {
        "firstName": "Test",
        "lastName": "User",
        "email": f"{uuid.uuid4()}@fake.com",
        "password": "myPassword"
    }

