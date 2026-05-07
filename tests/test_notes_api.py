#This file tests the notes API
from api.api_client import APIClient
from config.environment import load_config

#gets notes through API
def test_get_notes():

    config = load_config()

    api = APIClient()

    # login
    login_response = api.login(
        config["credentials"]["email"],
        config["credentials"]["password"]
    )

    assert login_response.status_code == 200

    
    notes_response = api.get_notes()

    
    assert notes_response.status_code == 200

    
    response_data = notes_response.json()

    assert "data" in response_data

    
    response_time = notes_response.elapsed.total_seconds()

    print(f"\nAPI Response Time: {response_time} seconds")

    assert response_time < 15