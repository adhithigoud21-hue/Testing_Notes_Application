from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    login_link = (By.LINK_TEXT, "Login")

    email_input = (By.NAME, "email")

    password_input = (By.NAME, "password")

    login_button = (
        By.XPATH,
        "//button[contains(text(),'Login')]"
    )

    # Login Method
    def login(self, email, password):

        wait = WebDriverWait(self.driver, 20)

        # Click Login link first
        login_link_element = wait.until(
            EC.element_to_be_clickable(
                self.login_link
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            login_link_element
        )

        # Email
        email_field = wait.until(
            EC.visibility_of_element_located(
                self.email_input
            )
        )

        email_field.clear()
        email_field.send_keys(email)

        # Password
        password_field = wait.until(
            EC.visibility_of_element_located(
                self.password_input
            )
        )

        password_field.clear()
        password_field.send_keys(password)

        # Login button
        login_btn = wait.until(
            EC.element_to_be_clickable(
                self.login_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            login_btn
        )