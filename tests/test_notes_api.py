from api.api_client import APIClient
from config.environment import load_config


def test_get_notes():

    config = load_config()

    api = APIClient()

    # Login API
    login_response = api.login(
        config["credentials"]["email"],
        config["credentials"]["password"]
    )

    assert login_response.status_code == 200

    # Get Notes
    notes_response = api.get_notes()

    # Status validation
    assert notes_response.status_code == 200

    # Response structure validation
    response_data = notes_response.json()

    assert "data" in response_data

    # Response time validation (< 2 sec)
    response_time = notes_response.elapsed.total_seconds()

    print(f"\nAPI Response Time: {response_time} seconds")

    assert response_time < 2