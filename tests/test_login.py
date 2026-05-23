import allure
from pages.login_page import LoginPage

@allure.feature("Login Feature")
@allure.story("Valid Login")
def test_valid_login(page, config):

    login = LoginPage(page)

    with allure.step("Open Login Page"):
        login.open(config["base_url"])

    with allure.step("Perform Login"):
        login.login("Admin", "admin123")

    with allure.step("Validate Dashboard"):
        page.wait_for_timeout(3000)
        assert "dashboard" in page.url.lower()