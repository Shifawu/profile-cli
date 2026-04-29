import requests
import sys

BASE_URL = "https://gender-classification-api-production.up.railway.app/"


def get_profiles():
    token = input("Enter your access token: ")

    res = requests.get(
        f"{BASE_URL}/profiles/?limit=5",
        headers={"Authorization": f"Bearer {token}"}
    )

    print(res.json())


def create_profile():
    token = input("Enter your access token: ")
    name = input("Enter name: ")

    res = requests.post(
        f"{BASE_URL}/profiles",
        json={"name": name},
        headers={"Authorization": f"Bearer {token}"}
    )

    print(res.json())


if __name__ == "__main__":
    print("1. Get Profiles")
    print("2. Create Profile")

    choice = input("Choose: ")

    if choice == "1":
        get_profiles()
    elif choice == "2":
        create_profile()