import json


def load_profile(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Profile JSON file not found.")
        return None

    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return None