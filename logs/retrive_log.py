import json

# Load JSON data
with open("C:/Users/VICTUS/Documents/ctk/logs/sign_in_log.json", "r") as f:
    data = json.load(f)

# Iterate through the data
for timestamp, user_info in data.items():
    # Skip "_comment" or any non-dictionary entries
    if not isinstance(user_info, dict):
        continue
    
    # Safely get the username
    username = user_info.get("username", "Unknown")
    logout = user_info.get("logout")
    print(f"Timestamp: {timestamp}, Username: {username}, {logout}")
