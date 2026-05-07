#This file has setup and teardown of browser and also has screenshot on failure
import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from config.environment import load_config


# Driver fixture with support for local and grid execution

@pytest.fixture
def driver():

    config = load_config()

    execution_mode = config["execution"]

    #local execution

    if execution_mode == "local":

        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            )
        )

    # grid execution

    elif execution_mode == "grid":

        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=webdriver.ChromeOptions()
        )

    else:
        raise Exception(
            "Invalid execution mode in config.yaml"
        )

    driver.maximize_window()

    driver.get(config["base_url"])

    yield driver

    driver.quit()


# Screenshot on failure 

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            
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