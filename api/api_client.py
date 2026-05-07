import requests
#This File Contains a API Client class which will be used for interactions

#This URL is API URL
BASE_URL = "https://practice.expandtesting.com/notes/api"


class APIClient:
#It is a constructor which calls itself when object of class is created
    def __init__(self):

        self.token = None

        self.headers = {
            "Content-Type": "application/json"
        }

    
#Used for Login and authentication
    def login(self, email, password):

        payload = {
            "email": email,
            "password": password
        }

        response = requests.post(
            f"{BASE_URL}/users/login",
            json=payload,
            timeout=30
        )
# if login success then token will get stored 
        
        if response.status_code == 200:

            response_json = response.json()

            if "data" in response_json:

                self.token = response_json["data"]["token"]

                self.headers = {
                    "Content-Type": "application/json",
                    "x-auth-token": self.token
                }

        return response
#used to get notes
    
    def get_notes(self):

        response = requests.get(
            f"{BASE_URL}/notes",
            headers=self.headers,
            timeout=30
        )

        return response

    
#used to create a note
    def create_note(self, title, description):

        payload = {
            "title": title,
            "description": description,
            "category": "Home"
        }

        response = requests.post(
            f"{BASE_URL}/notes",
            json=payload,
            headers=self.headers,
            timeout=30
        )

        return response

    
# used for deleting a note
    def delete_note(self, note_id):

        response = requests.delete(
            f"{BASE_URL}/notes/{note_id}",
            headers=self.headers,
            timeout=30
        )

        return response