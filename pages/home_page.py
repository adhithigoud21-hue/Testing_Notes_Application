from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    add_note_button = (
        By.XPATH,
        "//button[contains(text(),'Add Note')]"
    )

    title_input = (
        By.ID,
        "title"
    )

    description_input = (
        By.ID,
        "description"
    )

    save_button = (
        By.XPATH,
        "//button[@type='submit']"
    )

    # Create Note Method
    def create_note(self, title, description):

        wait = WebDriverWait(self.driver, 20)

        # Click Add Note
        add_btn = wait.until(
            EC.element_to_be_clickable(
                self.add_note_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add_btn
        )

        # Enter Title
        wait.until(
            EC.visibility_of_element_located(
                self.title_input
            )
        ).send_keys(title)

        # Enter Description
        wait.until(
            EC.visibility_of_element_located(
                self.description_input
            )
        ).send_keys(description)

        # Click Save
        save_btn = wait.until(
            EC.element_to_be_clickable(
                self.save_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            save_btn
        )

            # Get all notes text from UI
    def get_notes_text(self):

        return self.driver.page_source.lower()
        # Get total notes count
    def get_notes_count(self):

        notes = self.driver.find_elements(
            By.XPATH,
            "//div[contains(@class,'card')]"
        )

        return len(notes)
        # Open Add Note Form
    def open_add_note_form(self):

        wait = WebDriverWait(self.driver, 20)

        add_btn = wait.until(
            EC.element_to_be_clickable(
                self.add_note_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add_btn
        )


    # Click Save Without Data
    def save_empty_note(self):

        wait = WebDriverWait(self.driver, 20)

        save_btn = wait.until(
            EC.element_to_be_clickable(
                self.save_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            save_btn
        )