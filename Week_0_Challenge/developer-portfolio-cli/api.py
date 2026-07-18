import requests

def get_github_profile(username):
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            return response.json()

        return None

    except requests.exceptions.RequestException:
        return None