import pytest
from playwright.sync_api import Page, expect

@pytest.mark.ui
@pytest.mark.smoke
def test_saucedemo_valid_login(page: Page):
    """Verify that a standard user can successfully log into the dashboard."""
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")

@pytest.mark.ui
def test_saucedemo_locked_user_error(page: Page):
    """Verify that locked-out users receive the correct error message."""
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("locked_out_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    error_element = page.locator("[data-test='error']")
    expect(error_element).to_be_visible()
    expect(error_element).to_contain_text("Sorry, this user has been locked out.")
