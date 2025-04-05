import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from Utilities.report_utils import capture_screenshot


@pytest.fixture(scope="function")
def browser():
    # Initialize browser
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    # Teardown
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get('browser')
        if driver is not None:
            screenshot_path = capture_screenshot(driver, report.nodeid)
            report.sections.append(("Screenshot", f"<img src='{screenshot_path}'/>"))