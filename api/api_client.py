import requests

BASE_URL = "https://practice.expandtesting.com/notes/api"


class APIClient:

    def __init__(self):

        self.token = None

        self.headers = {
            "Content-Type": "application/json"
        }

    # ---------------- LOGIN API ----------------

    def login(self, email, password):

        payload = {
            "email": email,
            "password": password
        }

        response = requests.post(
            f"{BASE_URL}/users/login",
            json=payload
        )

        # Store token only if login successful
        if response.status_code == 200:

            response_json = response.json()

            if "data" in response_json:

                self.token = response_json["data"]["token"]

                self.headers = {
                    "Content-Type": "application/json",
                    "x-auth-token": self.token
                }

        return response

    # ---------------- GET NOTES API ----------------

    def get_notes(self):

        response = requests.get(
            f"{BASE_URL}/notes",
            headers=self.headers
        )

        return response

    # ---------------- CREATE NOTE API ----------------

    def create_note(self, title, description):

        payload = {
            "title": title,
            "description": description,
            "category": "Home"
        }

        response = requests.post(
            f"{BASE_URL}/notes",
            json=payload,
            headers=self.headers
        )

        return response

    # ---------------- DELETE NOTE API ----------------

    def delete_note(self, note_id):

        response = requests.delete(
            f"{BASE_URL}/notes/{note_id}",
            headers=self.headers
        )

        return response