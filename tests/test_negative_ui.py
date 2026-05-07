#This file will have the negative test cases for UI
from pages.login_page import LoginPage
from pages.home_page import HomePage

from config.environment import load_config

import time


# Tests invalid login credentials

def test_invalid_login(driver):

    login = LoginPage(driver)

    login.login(
        "wrong@gmail.com",
        "wrongpassword"
    )

    time.sleep(3)

    page_source = driver.page_source.lower()

    assert (
        "invalid" in page_source
        or
        "incorrect" in page_source
        or
        "error" in page_source
    )

#Tests blank credentials


def test_login_with_blank_email(driver):

    config = load_config()

    login = LoginPage(driver)

    login.login(
        "",
        config["credentials"]["password"]
    )

    time.sleep(2)

    assert "login" in driver.current_url.lower()


#Tests creation of note with only description
def test_create_note_with_only_description(driver):

    config = load_config()

    login = LoginPage(driver)

    login.login(
        config["credentials"]["email"],
        config["credentials"]["password"]
    )

    home = HomePage(driver)

    home.create_note(
        "",
        "Only Description"
    )

    #time.sleep(2)

    assert "notes" in driver.current_url.lower()