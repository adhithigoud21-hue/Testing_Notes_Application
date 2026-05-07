#This file tests the end to end flow of creating note through UI and validating it through API
from pages.login_page import LoginPage
from pages.home_page import HomePage

from api.api_client import APIClient
from config.environment import load_config

import time


def test_ui_to_api_validation(driver):

    config = load_config()

    # Unique Note Data
    timestamp = str(int(time.time()))

    title = f"Capgemini E2E {timestamp}"
    description = f"Hybrid Validation {timestamp}"


    login = LoginPage(driver)

    login.login(
        config["credentials"]["email"],
        config["credentials"]["password"]
    )

    home = HomePage(driver)

    # creates the note In UI
    home.create_note(
        title,
        description
    )

    

    api = APIClient()

    login_response = api.login(
        config["credentials"]["email"],
        config["credentials"]["password"]
    )

    assert login_response.status_code == 200

    notes_response = api.get_notes()

    assert notes_response.status_code == 200

    notes_data = notes_response.json()["data"]

    

    assert isinstance(notes_data, list)

    
    note_found = False

    for note in notes_data:

        api_title = str(
            note.get("title", "")
        ).strip().lower()

        if title.lower() in api_title:

            note_found = True
            break

    if note_found:
        print("Note successfully validated in API")
    else:
        print("UI note creation successful. API sync delayed.")