from utils import load_profile
from api import get_github_profile


def display_profile(profile):
    print("\n" + "=" * 45)
    print("        DEVELOPER PORTFOLIO")
    print("=" * 45)

    print(f"Name       : {profile['name']}")
    print(f"Nickname   : {profile['nickname']}")
    print(f"Role       : {profile['role']}")
    print(f"University : {profile['university']}")
    print(f"Department : {profile['department']}")
    print(f"Year       : {profile['year']}")

    print("\nSkills")
    for skill in profile["skills"]:
        print(f"  • {skill}")

    print(f"\nGitHub    : {profile['github']}")
    print(f"Portfolio : {profile['portfolio']}")
    print(f"Email     : {profile['email']}")


def search_github():
    username = input("\nEnter GitHub Username: ").strip()

    data = get_github_profile(username)

    if data is None:
        print("\nGitHub user not found.")
        return

    print("\n" + "-" * 45)
    print("          GITHUB PROFILE")
    print("-" * 45)

    print(f"Username            : {data['login']}")
    print(f"Name                : {data.get('name')}")
    print(f"Bio                 : {data.get('bio')}")
    print(f"Followers           : {data['followers']}")
    print(f"Following           : {data['following']}")
    print(f"Public Repositories : {data['public_repos']}")
    print(f"Profile URL         : {data['html_url']}")


def menu():
    profile = load_profile("profile.json")

    if profile is None:
        return

    while True:
        print("\n" + "=" * 45)
        print("     Developer Portfolio CLI")
        print("=" * 45)
        print("1. View Portfolio")
        print("2. Search GitHub Profile")
        print("3. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            display_profile(profile)

        elif choice == "2":
            search_github()

        elif choice == "3":
            print("\nThank you for using Developer Portfolio CLI!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    menu()