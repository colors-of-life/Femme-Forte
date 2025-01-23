import requests
import json
from typing import Tuple, Optional

def log_state_check() -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """Checks the log state from the API and returns state, user, and system_name."""

    try:
        # Load config
        with open("./config/config.json") as f:
            data = json.load(f)
        
        base_url = data.get("url", "")
        if not base_url:
            raise ValueError("Base URL not found in config.")

        endpoint = "/log-state-check"
        url = f"{base_url}{endpoint}"

        with open(".\\config\\config.json") as f:
            data = json.load(f)

        params = {"client_name": f"{data["client_name"]}"}

        # Make the request
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for HTTP errors
        
        # Parse JSON response
        data = response.json()

        # Safely retrieve keys
        return (
            data.get("state"),
            data.get("user"),
            data.get("system_name"),
        )

    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Config or JSON error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"HTTP request exception: {e}")
        try:
            data = response.json()
            print(data["message"])
        except Exception:
            print("Check your connection")
    except KeyError as e:
        print(f"Missing key in response: {e}")
    except ValueError as e:
        print(f"Configuration error: {e}")

    # Return defaults in case of failure
    return None, None, None
