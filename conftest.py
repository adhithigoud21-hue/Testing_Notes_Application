import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from config.environment import load_config


# ---------------- DRIVER FIXTURE ----------------

@pytest.fixture
def driver():

    config = load_config()

    driver_path = ChromeDriverManager().install()

    driver_path = os.path.join(
        os.path.dirname(driver_path),
        "chromedriver.exe"
    )

    driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=webdriver.ChromeOptions()
)

    driver.maximize_window()

    driver.get(config["base_url"])

    yield driver

    driver.quit()


# ---------------- SCREENSHOT ON FAILURE ----------------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            # Create screenshots folder
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            screenshot_path = (
                f"screenshots/{item.name}.png"
            )

            driver.save_screenshot(
                screenshot_path
            )

            print(
                f"\nScreenshot saved: {screenshot_path}"
            )