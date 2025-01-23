import requests
import json

def send_sign_up_data(data:dict) ->None:
    with open(".\\config\\config.json", "r") as f:
        config_data = json.load(f)
        client_name = config_data['client_name']
        base_url = config_data['url']
    
    endpoint = "/send-up-data"
    url =f"{base_url}{endpoint}"

    data["client_name"] = client_name

    response = requests.post(url, json= data)
    
    if response.status_code == 200:
        print("S")
    else:
        print("f")

