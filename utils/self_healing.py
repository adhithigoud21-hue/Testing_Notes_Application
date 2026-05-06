from selenium.webdriver.common.by import By


class SelfHealingLocator:

    @staticmethod
    def find_element(
        driver,
        primary_locator,
        fallback_locator=None
    ):

        try:

            return driver.find_element(
                *primary_locator
            )

        except:

            if fallback_locator:

                return driver.find_element(
                    *fallback_locator
                )

            raise Exception(
                "Element not found"
            )