from pages.login_page import LoginPage
from pages.home_page import HomePage
from config.environment import load_config
import time


def test_create_note(driver):

    config = load_config()

    login = LoginPage(driver)

    login.login(
        config["credentials"]["email"],
        config["credentials"]["password"]
    )

    # wait after login
    time.sleep(3)

    home = HomePage(driver)

    home.create_note(
        "Capgemini Note",
        "This is automation testing project"
    )

    assert "notes" in driver.current_url