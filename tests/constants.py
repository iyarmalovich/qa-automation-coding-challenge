from config.settings import BASE_URL, USERNAME, PASSWORD

CONTACTS_ENDPOINT = f"{BASE_URL}/contacts"


USER_ENDPOINT = f"{BASE_URL}/users"

VALID_CREDENTIALS = {
    "email": f"{USERNAME}",
    "password": f"{PASSWORD}"
}


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

UPDATED_DATA = {
    "firstName": "Amy",
    "lastName": "Miller",
    "birthdate": "1992-02-02",
    "email": "amiller@fake.com",
    "phone": "8005554242",
    "street1": "13 School St.",
    "street2": "Apt. 5",
    "city": "Washington",
    "stateProvince": "QC",
    "postalCode": "03-083",
    "country": "Canada"
}

INVALID_CREDENTIALS = {
    "email": "test2@fake.com",
    "password": "wrongPassword"
}
