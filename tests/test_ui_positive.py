from config.settings import USERNAME, PASSWORD



def test_login_valid_credentials(browser):
    """Test login with valid credentials."""
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://thinking-tester-contact-list.herokuapp.com")
    page.fill("input[id='email']", f"{USERNAME}")
    page.fill("input[id='password']", f"{PASSWORD}")
    page.click("button[id='submit']")

    page.wait_for_selector("div.contacts")  # Wait for the contacts container to load
    assert page.is_visible("div.contacts"), "Contacts page did not load"

    # Step 3: Verify contacts table visibility
    assert page.locator("#myTable").is_visible(), "Contacts table is not visible"

    # Optional: Log table content for debugging
    table_content = page.locator("#myTable").inner_text()
    print(f"Contacts table content:\n{table_content}")

    context.close()

    context.close()


def test_create_contact(browser):
    """Test creating a new contact."""
    # Step 1: Create a new browser context and page
    context = browser.new_context()
    page = context.new_page()

    # Step 2: Log in to the application
    page.goto("https://thinking-tester-contact-list.herokuapp.com")
    page.fill("input[id='email']", f"{USERNAME}")
    page.fill("input[id='password']", f"{PASSWORD}")
    page.click("button[id='submit']")
    page.wait_for_selector("div.contacts", timeout=10000)  # Wait for up to 10 seconds

    # Step 3: Verify contacts table visibility
    assert page.locator("#myTable").is_visible(), "Contacts table is not visible"
    table_content = page.locator("#myTable").inner_text()
    print(f"Contacts table content before adding contact:\n{table_content}")

    # Step 4: Navigate to the "Create Contact" page
    page.click("button[id='add-contact']")

    # Step 5: Fill in the contact creation form
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

    # Step 6: Verify the new contact appears in the contacts table
    page.wait_for_selector("div.contacts", timeout=10000)  # Wait for up to 10 seconds
    assert page.locator("#myTable").is_visible(), "Contacts table is not visible"

    table_content = page.locator("#myTable").inner_text()
    print(f"Contacts table content after adding contact:\n{table_content}")
    assert "testName" in table_content, "New contact was not added to the table"
    context.close()
