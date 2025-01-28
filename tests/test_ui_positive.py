from config.settings import USERNAME, PASSWORD



def test_login_valid_credentials(browser):
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://thinking-tester-contact-list.herokuapp.com")
    page.fill("input[id='email']", f"{USERNAME}")
    page.fill("input[id='password']", f"{PASSWORD}")
    page.click("button[id='submit']")

    page.wait_for_selector("div.contacts")
    assert page.is_visible("div.contacts"), "Contacts page did not load"

    assert page.locator("#myTable").is_visible(), "Contacts table is not visible"

    table_content = page.locator("#myTable").inner_text()
    print(f"Contacts table content:\n{table_content}")

    context.close()

    context.close()


def test_create_contact(browser):
    """Test creating a new contact."""
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://thinking-tester-contact-list.herokuapp.com")
    page.fill("input[id='email']", f"{USERNAME}")
    page.fill("input[id='password']", f"{PASSWORD}")
    page.click("button[id='submit']")
    page.wait_for_selector("div.contacts", timeout=10000)

    assert page.locator("#myTable").is_visible(), "Contacts table is not visible"
    table_content = page.locator("#myTable").inner_text()
    print(f"Contacts table content before adding contact:\n{table_content}")

    page.click("button[id='add-contact']")

    page.fill("input[id='firstName']", "testName")
    page.fill("input[id='lastName']", "testLastName")
    page.fill("input[id='email']", "test@fake.com")
    page.fill("input[id='phone']", "000000000")
    page.fill("input[id='birthdate']", "2002-02-02")
    page.fill("input[id='street1']", "testStreet1")
    page.fill("input[id='city']", "testCity")
    page.fill("input[id='stateProvince']", "TS")
    page.fill("input[id='postalCode']", "00000")
    page.fill("input[id='country']", "TST")
    page.click("button[id='submit']")

    page.wait_for_selector("div.contacts", timeout=10000)
    assert page.locator("#myTable").is_visible(), "Contacts table is not visible"

    table_content = page.locator("#myTable").inner_text()
    print(f"Contacts table content after adding contact:\n{table_content}")
    assert "testName" in table_content, "New contact was not added to the table"
    context.close()
