from config.settings import USERNAME, PASSWORD


def test_login_invalid_credentials(browser):
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://thinking-tester-contact-list.herokuapp.com")
    page.fill("input[id='email']", "invalid@fake.com")
    page.fill("input[id='password']", "invalidPassword")
    page.click("button[id='submit']")

    # Verify error message
    page.wait_for_selector("#error")
    assert "Incorrect username or password" in page.text_content("#error"), "Error message not displayed for invalid credentials"

    context.close()


def test_create_contact_missing_required_fields(browser):
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://thinking-tester-contact-list.herokuapp.com")
    page.fill("input[id='email']", f"{USERNAME}")
    page.fill("input[id='password']", f"{PASSWORD}")
    page.click("button[id='submit']")
    page.wait_for_selector("div.contacts")

    page.click("button[id='add-contact']")

    page.fill("input[id='email']", "indalid@fake.com")
    page.click("button[id='submit']")

    page.wait_for_selector("#error")
    assert "Contact validation failed: firstName: Path `firstName` is required., lastName: Path `lastName` is required." in page.text_content("#error"), "Error message not displayed for missing required fields"

    context.close()


def test_create_contact_invalid_email(browser):
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://thinking-tester-contact-list.herokuapp.com")
    page.fill("input[id='email']", f"{USERNAME}")
    page.fill("input[id='password']", f"{PASSWORD}")
    page.click("button[id='submit']")
    page.wait_for_selector("div.contacts")

    page.click("button[id='add-contact']")
    page.fill("input[id='firstName']", "validName")
    page.fill("input[id='lastName']", "validLastName")
    page.fill("input[id='email']", "invalid_email")
    page.click("button[id='submit']")

    page.wait_for_selector("#error")
    assert "Contact validation failed: email: Email is invalid" in page.text_content("#error"), "Error message not displayed for invalid email"

    context.close()