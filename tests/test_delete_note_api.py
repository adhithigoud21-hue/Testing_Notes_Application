# This file has delete note from API and validate in UI(E2E)

from pages.login_page import LoginPage
from pages.home_page import HomePage

from api.api_client import APIClient
from config.environment import load_config

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
#This will clos ethe  popup

def close_popup(driver):

    try:

        wait = WebDriverWait(driver, 5)

        close_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//*[contains(text(),'Close')]"
                )
            )
        )

        close_button.click()

        time.sleep(2)

    except:
        pass


# This method deletes note and validates in UI
def test_delete_note_api(driver):

    config = load_config()

    timestamp = str(int(time.time()))

    
    title = f"Delete Note {timestamp}"

    description = f"Delete API Validation {timestamp}"

    

    api = APIClient()

    login_response = api.login(
        config["credentials"]["email"],
        config["credentials"]["password"]
    )

    assert login_response.status_code == 200

    # Creates note through API

    create_response = api.create_note(
        title,
        description
    )

    assert create_response.status_code == 200

    note_id = create_response.json()["data"]["id"]

    # Login to UI

    login = LoginPage(driver)

    login.login(
        config["credentials"]["email"],
        config["credentials"]["password"]
    )

    home = HomePage(driver)

    time.sleep(5)

    close_popup(driver)

    driver.refresh()

    time.sleep(5)

    close_popup(driver)

    page_text = home.get_notes_text()

    print("\nPAGE TEXT:\n", page_text)

    # Validate note whether exists
    assert title.lower() in page_text

    # delete the note through API

    delete_response = api.delete_note(note_id)

    assert delete_response.status_code in [200, 204]

    time.sleep(5)

    # refresh the page

    driver.refresh()

    time.sleep(5)

    close_popup(driver)

    updated_text = home.get_notes_text()

    print("\nUPDATED PAGE TEXT:\n", updated_text)

    # validates
    assert title.lower() not in updated_text