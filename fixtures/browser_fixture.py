import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#This file has setup and teardown of browser
@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://practice.expandtesting.com/notes/app")
    yield driver
    driver.quit()