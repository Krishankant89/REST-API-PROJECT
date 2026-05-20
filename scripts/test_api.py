import requests

BASE_URL = "http://127.0.0.1:8000"


def test_health():
    response = requests.get(f"{BASE_URL}/")

    print("Health Check:")
    print(response.status_code)
    print(response.json())


def create_task():
    payload = {
        "title": "Learn Kubernetes",
        "description": "Practice Deployments and Services"
    }

    response = requests.post(
        f"{BASE_URL}/tasks/",
        json=payload
    )

    print("\nCreate Task:")
    print(response.status_code)
    print(response.json())


def get_tasks():
    response = requests.get(f"{BASE_URL}/tasks/")

    print("\nGet Tasks:")
    print(response.status_code)
    print(response.json())


if __name__ == "__main__":
    test_health()
    create_task()
    get_tasks()