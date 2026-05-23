import pytest
import yaml
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml") as file:
        return yaml.safe_load(file)

@pytest.fixture(scope="function")
def page(config):

    with sync_playwright() as p:

        browser_type = getattr(p, config["browser"])

        browser = browser_type.launch(
            headless=config["headless"]
        )

        context = browser.new_context(
            record_video_dir="reports/videos/"
        )

        page = context.new_page()

        yield page

        context.close()
        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:
            page.screenshot(
                path=f"screenshots/{item.name}.png"
            )