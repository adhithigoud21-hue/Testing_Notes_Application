import requests

BASE_URL = "https://practice.expandtesting.com/notes/api"


class APIClient:

    def __init__(self):
        self.token = None

    # Login API
    def login(self, email, password):

        payload = {
            "email": email,
            "password": password
        }

        response = requests.post(
            f"{BASE_URL}/users/login",
            json=payload
        )

        self.token = response.json()["data"]["token"]

        return response

    # Get Notes API
    def get_notes(self):

        headers = {
            "x-auth-token": self.token
        }

        response = requests.get(
            f"{BASE_URL}/notes",
            headers=headers
        )

        return response
    
        # Create Note API
    def create_note(self, title, description):

        headers = {
            "x-auth-token": self.token
        }

        payload = {
            "title": title,
            "description": description,
            "category": "Home"
        }

        response = requests.post(
            f"{BASE_URL}/notes",
            json=payload,
            headers=headers
        )

        return response


    # Delete Note API
    def delete_note(self, note_id):

        headers = {
            "x-auth-token": self.token
        }

        response = requests.delete(
            f"{BASE_URL}/notes/{note_id}",
            headers=headers
        )

        return response
    