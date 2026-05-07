#This file will test the login
from pages.login_page import LoginPage
from config.environment import load_config

from utils.logger import setup_logger


logger = setup_logger()


def test_login(driver):

    logger.info("Starting Login Test")

    config = load_config()

    login = LoginPage(driver)

    login.login(
        config["credentials"]["email"],
        config["credentials"]["password"]
    )

    logger.info("Login successful")

    assert "notes" in driver.current_url

    logger.info("Login Test Passed")