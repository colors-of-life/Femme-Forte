import requests
import json

class LoginAuthClient:
    def __init__(self):

        with open(".\\config\\config.json") as f:
            data = json.load(f)

        self.base_url = data["url"]
        self.status = ""

    def login(self, username, password, remember):
        endpoint = "/login"
        url = f"{self.base_url}{endpoint}"

        with open(".\\config\\config.json", 'r') as f:
            data = json.load(f)

        payload = {
            "username": username,
            "password": password,
            "remember": remember,
            "client_name" : data["client_name"]
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 400:
                self.status = "failed-user-pass-missing"
            elif response.status_code == 200:
                print("Success:", response.json())
                self.status = "verified"
            elif response.status_code == 401:
                print("Failed:", response.json())
                self.status = "failed-username"
            elif response.status_code == 402:
                print("Failed:", response.json())
                self.status = "failed-password"
            else:
                print("Unexpected response:", response.status_code, response.text)
        except requests.exceptions.RequestException as e:
            print("Error:", e)


# Entry point for the client
if __name__ == "__main__":
    # Change this to your Flask server's URL
    base_url = "https://classic-rat-firstly.ngrok-free.app"
    client = LoginAuthClient(base_url)

    # Test login with valid credentials
    print("Testing with valid credentials:")
    client.login("testuser1", "testpass1", "false")

    # Test login with invalid credentials
    print("\nTesting with invalid credentials:")
    client.login("testuser2", "testpass2", "true")
