import time
import requests

from api.api_client import APIClient
from config.environment import load_config


config = load_config()

BASE_URL = config["api_url"]


# ---------------- API PERFORMANCE ----------------

def test_api_response_time():

    start_time = time.time()

    response = requests.get(
        f"{BASE_URL}/health-check"
    )

    end_time = time.time()

    response_time = (
        end_time - start_time
    )

    print(
        f"\nAPI Response Time: {response_time}"
    )

    assert response_time < 5


# ---------------- UI PERFORMANCE ----------------

def test_ui_page_load_time(driver):

    start_time = time.time()

    driver.get(
        config["base_url"]
    )

    end_time = time.time()

    load_time = (
        end_time - start_time
    )

    print(
        f"\nUI Load Time: {load_time}"
    )

    assert load_time < 10