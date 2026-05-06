import requests

from api.api_client import APIClient
from config.environment import load_config


config = load_config()

BASE_URL = config["api_url"]


# ---------------- INVALID TOKEN ----------------

def test_invalid_token():

    headers = {
        "x-auth-token": "invalidtoken"
    }

    response = requests.get(
        f"{BASE_URL}/notes",
        headers=headers
    )

    assert response.status_code in [401, 403]


# ---------------- INVALID ENDPOINT ----------------

def test_invalid_endpoint():

    response = requests.get(
        f"{BASE_URL}/invalidendpoint"
    )

    assert response.status_code == 404


# ---------------- INVALID LOGIN ----------------

def test_login_with_invalid_email():

    api = APIClient()

    response = api.login(
        "wrong@gmail.com",
        "wrongpass"
    )

    assert response.status_code in [400, 401]


# ---------------- BLANK LOGIN ----------------

def test_login_with_blank_credentials():

    api = APIClient()

    response = api.login(
        "",
        ""
    )

    assert response.status_code in [400, 401]


# ---------------- ACCESS WITHOUT LOGIN ----------------

def test_get_notes_without_login():

    response = requests.get(
        f"{BASE_URL}/notes"
    )

    assert response.status_code in [401, 403]


# ---------------- EMPTY NOTE CREATION ----------------

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