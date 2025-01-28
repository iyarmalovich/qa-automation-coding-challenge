import requests

from logger import logger
from tests.constants import CONTACTS_ENDPOINT, NEW_CONTACT, UPDATED_DATA


def test_create_contact(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(CONTACTS_ENDPOINT, json=NEW_CONTACT, headers=headers)
    assert response.status_code == 201

    response_data = response.json()
    assert "_id" in response_data
    assert response_data["firstName"] == NEW_CONTACT["firstName"]
    assert response_data["lastName"] == NEW_CONTACT["lastName"]
    assert response_data["email"] == NEW_CONTACT["email"]


def test_create_contact_with_incorrect_content(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(CONTACTS_ENDPOINT, json={"firstName": "Leo",}, headers=headers)
    assert response.status_code == 400

    response_data = response.json()
    assert response_data["message"] == 'Contact validation failed: lastName: Path `lastName` is required.'


def test_get_contacts(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(CONTACTS_ENDPOINT, headers=headers)

    assert response.status_code == 200

    contacts = response.json()
    assert isinstance(contacts, list)

    required_fields = [
        "_id", "firstName", "lastName", "birthdate", "email",
        "phone", "street1", "city", "stateProvince", "postalCode", "country", "owner"
    ]
    for field in required_fields:
        assert field in contacts[0]


def test_update_contact(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(CONTACTS_ENDPOINT, json=NEW_CONTACT, headers=headers)
    response_id = response.json()["_id"]

    response = requests.put(f"{CONTACTS_ENDPOINT}/{response_id}", headers=headers, json=UPDATED_DATA)

    assert response.status_code == 200
    response_data = response.json()

    for key, value in UPDATED_DATA.items():
        assert response_data.get(key) == value

    required_fields = ["_id", "owner", "__v"]
    for field in required_fields:
        assert field in response_data


def test_update_contact_not_found(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.put(f"{CONTACTS_ENDPOINT}/not-exist", headers=headers, json=UPDATED_DATA)

    assert response.status_code == 400


def test_delete_contact_success(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}

    logger.info("Creating a contact for deletion test")
    create_response = requests.post(CONTACTS_ENDPOINT, json=NEW_CONTACT, headers=headers)

    contact_id = create_response.json().get("_id")

    logger.info(f"Deleting contact with ID {contact_id}")
    delete_response = requests.delete(f"{CONTACTS_ENDPOINT}/{contact_id}", headers=headers)

    logger.info("Received response: status = %d, body = %s", delete_response.status_code, delete_response.text)

    assert delete_response.status_code == 200
    logger.info("Contact successfully deleted")
