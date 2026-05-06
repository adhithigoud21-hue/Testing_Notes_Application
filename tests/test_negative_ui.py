from pages.login_page import LoginPage
from pages.home_page import HomePage

from config.environment import load_config

import time


# ---------------- INVALID LOGIN ----------------

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


# ---------------- EMPTY NOTE CREATION ----------------

def test_empty_note_creation(driver):

    config = load_config()

    login = LoginPage(driver)

    login.login(
        config["credentials"]["email"],
        config["credentials"]["password"]
    )

    time.sleep(3)

    home = HomePage(driver)

    # Count notes before action
    before_count = home.get_notes_count()

    # Open note form
    home.open_add_note_form()

    time.sleep(2)

    # Save without entering data
    home.save_empty_note()

    time.sleep(3)

    # Count notes after action
    after_count = home.get_notes_count()

    # Validation
    assert before_count == after_count