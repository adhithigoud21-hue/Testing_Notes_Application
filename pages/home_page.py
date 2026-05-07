#This file contains the HomePage calss which has methods to interact with application's homepage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

#This Homepage contains methods of homepage
class HomePage:

    def __init__(self, driver):

        self.driver = driver

    # ---------------- LOCATORS ----------------

    notes_text = (By.TAG_NAME, "body")

    note_cards = (By.CLASS_NAME, "card")

    add_note_button = (
        By.XPATH,
        "//button[contains(text(),'Add Note')]"
    )

    title_input = (
        By.XPATH,
        "//input[@name='title']"
    )

    description_input = (
        By.XPATH,
        "//textarea[@name='description']"
    )

    save_button = (
        By.XPATH,
        "//button[contains(text(),'Create')]"
    )

    #This method helps to close the ads popup

    def close_popup(self):

        try:

            close_btn = WebDriverWait(
                self.driver,
                5
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//*[contains(text(),'Close')]"
                    )
                )
            )

            close_btn.click()

            time.sleep(2)

        except:
            pass

    #This method will get the text of notes

    def get_notes_text(self):

        self.close_popup()

        body = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.presence_of_element_located(
                self.notes_text
            )
        )

        return body.text.lower()

    #This method  will count the no.of notes

    def get_notes_count(self):

        self.close_popup()

        notes = self.driver.find_elements(
            *self.note_cards
        )

        return len(notes)

    #This method will create note with given title and description

    def open_add_note_form(self):

        self.close_popup()

        add_btn = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(
                self.add_note_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add_btn
        )

        time.sleep(2)

    #This method will create note

    def create_note(self, title, description):

        self.open_add_note_form()

        title_field = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.title_input
            )
        )

        title_field.clear()

        title_field.send_keys(title)

        description_field = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.description_input
            )
        )

        description_field.clear()

        description_field.send_keys(description)

        save_btn = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(
                self.save_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            save_btn
        )

        time.sleep(3)

    #This method will try to save note without entering title and description

    def save_empty_note(self):

        save_btn = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(
                self.save_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            save_btn
        )

        time.sleep(2)