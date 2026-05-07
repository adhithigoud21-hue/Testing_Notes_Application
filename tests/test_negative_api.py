#This file will ahve the negative cases of API
import requests

from api.api_client import APIClient
from config.environment import load_config


config = load_config()

BASE_URL = config["api_url"]


#Tests invalid token

def test_invalid_token():

    headers = {
        "x-auth-token": "invalidtoken"
    }

    response = requests.get(
        f"{BASE_URL}/notes",
        headers=headers
    )

    assert response.status_code in [401, 403]





# Tests with invalid email

def test_login_with_invalid_email():

    api = APIClient()

    response = api.login(
        "wrong@gmail.com",
        "wrongpass"
    )

    assert response.status_code in [400, 401]


# Testrs with blank credentials

def test_login_with_blank_credentials():

    api = APIClient()

    response = api.login(
        "",
        ""
    )

    assert response.status_code in [400, 401]





#tests with empty note 

def test_create_note_with_empty_data():

    api = APIClient()

    api.login(
        "adhithigoud21@gmail.com",
        "9949959878"
    )

    payload = {
        "title": "",
        "description": ""
    }

    response = requests.post(
        f"{BASE_URL}/notes",
        json=payload,
        headers=api.headers
    )

    assert response.status_code in [400, 422]