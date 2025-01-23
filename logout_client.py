import requests

class LogOutClient:
    def __init__(self):
        self.base_url = "https://classic-rat-firstly.ngrok-free.app"
        self.status:str = ""

    def logout(self):
        endpoint = "/logout"
        url = f"{self.base_url}{endpoint}"

        try:
            response = requests.post(url)
            
        
        except requests.exceptions.RequestException as e:
            print("Error:", e)