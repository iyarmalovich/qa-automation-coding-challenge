import requests
import pytest

from config.settings import BASE_URL

CONTACTS_ENDPOINT = f"{BASE_URL}/contacts"

NEW_CONTACT = {
    "firstName": "Leo",
    "lastName": "Newton",
    "birthdate": "2004-04-05",
    "email": "leonewton@fake.com",
    "phone": "123456789",
    "street1": "Mokotowska 27",
    "street2": "Apartment 3",
    "city": "Waw",
    "stateProvince": "MO",
    "postalCode": "12-345",
    "country": "PL"
}

def test_create_contact(auth_token):
    """Test creating a new contact using a valid token."""
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(CONTACTS_ENDPOINT, json=NEW_CONTACT, headers=headers)
    assert response.status_code == 201, "Expected HTTP status code 201 for successful contact creation"

    response_data = response.json()
    assert "_id" in response_data, "'_id' field is missing in the response"
    assert response_data["firstName"] == NEW_CONTACT["firstName"], "First name does not match"
    assert response_data["lastName"] == NEW_CONTACT["lastName"], "Last name does not match"
    assert response_data["email"] == NEW_CONTACT["email"], "Email does not match"
