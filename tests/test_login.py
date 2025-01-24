import logging
import requests
from config.settings import BASE_URL

# Configure the logger
logger = logging.getLogger(__name__)

def test_login_success(auth_token):
    assert auth_token is not None, "Auth token should not be None"
    print(f"Auth token: {auth_token}")

    """
    Test successful login using a valid token.
    """
    logger.info("Starting test: test_login_success")

    # Example protected endpoint
    url = f"{BASE_URL}/v1/protected-endpoint"

    # Send a GET request with the auth token
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(url, headers=headers)

    # Assert the response is successful
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    logger.info("Test passed: test_login_success")


def test_login_failure():
    """
    Test login failure with invalid credentials.
    """
    logger.info("Starting test: test_login_failure")

    # Simulate invalid login credentials
    url = f"{BASE_URL}/v1/login"
    payload = {"username": "wrong_user", "password": "wrong_password"}
    response = requests.post(url, json=payload)

    # Assert the response indicates failure
    assert response.status_code == 401, f"Expected status code 401, got {response.status_code}"
    logger.info("Test passed: test_login_failure")


def test_token_expired(auth_token):
    """
    Test behavior when the token is expired.
    """
    logger.info("Starting test: test_token_expired")

    # Example endpoint
    url = f"{BASE_URL}/v1/protected-endpoint"

    # Simulate an expired token
    headers = {"Authorization": "Bearer expired_token"}
    response = requests.get(url, headers=headers)

    # Assert the response indicates unauthorized
    assert response.status_code == 401, f"Expected status code 401, got {response.status_code}"
    logger.info("Test passed: test_token_expired")