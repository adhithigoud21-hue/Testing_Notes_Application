#This file has Login page help to interact with application's login page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


class LoginPage:

    def __init__(self, driver):

        self.driver = driver


    login_link = (
        By.LINK_TEXT,
        "Login"
    )

    email_input = (
        By.NAME,
        "email"
    )

    password_input = (
        By.NAME,
        "password"
    )

    login_button = (
        By.XPATH,
        "//button[contains(text(),'Login')]"
    )

    #This will close the popup ads

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

    #This method will help to authenticate user through UI

    def login(self, email, password):

        wait = WebDriverWait(self.driver, 20)

        self.close_popup()

        
        try:

            login_link_element = wait.until(
                EC.element_to_be_clickable(
                    self.login_link
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                login_link_element
            )

        except:
            pass

        self.close_popup()

        email_field = wait.until(
            EC.visibility_of_element_located(
                self.email_input
            )
        )

        email_field.clear()

        email_field.send_keys(email)

        password_field = wait.until(
            EC.visibility_of_element_located(
                self.password_input
            )
        )

        password_field.clear()

        password_field.send_keys(password)

        login_btn = wait.until(
            EC.element_to_be_clickable(
                self.login_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            login_btn
        )

        time.sleep(3)