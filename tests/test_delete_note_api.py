from pages.login_page import LoginPage
from pages.home_page import HomePage

from api.api_client import APIClient
from config.environment import load_config

import time


def test_delete_note_api(driver):

    config = load_config()

    timestamp = str(int(time.time()))

    title = f"Delete Note {timestamp}"
    description = "Delete API Validation"

    # ---------------- API LOGIN ----------------

    api = APIClient()

    login_response = api.login(
        config["credentials"]["email"],
        config["credentials"]["password"]
    )

    assert login_response.status_code == 200

    # ---------------- CREATE NOTE VIA API ----------------

    create_response = api.create_note(
        title,
        description
    )

    assert create_response.status_code == 200

    note_id = create_response.json()["data"]["id"]

    # ---------------- LOGIN UI ----------------

    login = LoginPage(driver)

    login.login(
        config["credentials"]["email"],
        config["credentials"]["password"]
    )

    home = HomePage(driver)

    time.sleep(5)

    # Verify note appears before deletion
    page_text = home.get_notes_text()

    assert title.lower() in page_text

    # ---------------- DELETE NOTE VIA API ----------------

    delete_response = api.delete_note(note_id)

    assert delete_response.status_code in [200, 204]

    time.sleep(5)

    # ---------------- REFRESH UI ----------------

    driver.refresh()

    time.sleep(5)

    updated_text = home.get_notes_text()

    # ---------------- VALIDATION ----------------

    assert title.lower() not in updated_text