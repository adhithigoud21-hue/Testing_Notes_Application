import requests

from api.api_client import APIClient
from config.environment import load_config


BASE_URL = "https://practice.expandtesting.com/notes/api"


# ---------------- INVALID TOKEN ----------------

def test_invalid_token():

    headers = {
        "x-auth-token": "invalidtoken123"
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