#!/usr/bin/python3
"""
Returns information on a given employee
"""
import json
import requests
import sys


def fetch_data(url):
    """Fetches data from URL"""
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data from {url}")
        sys.exit(3)
    return response.json()


def main():
    """Main function to save an employee's info to a JSON file"""
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} [ID]")
        sys.exit(1)

    try:
        ID = int(sys.argv[1])
    except ValueError:
        print("Invalid ID")
        sys.exit(2)

    todo_url = f"https://jsonplaceholder.typicode.com/users/{ID}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{ID}"

    user_data = fetch_data(user_url)
    todo_data = fetch_data(todo_url)

    if not user_data:
        print(f"No data found for user with ID {ID}")
        sys.exit(4)

    name = user_data.get('username')

    if not name:
        print(f"User with ID {ID} does not have a name.")
        sys.exit(5)

    user_tasks = []

    for task in todo_data:
        task_info = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": name
        }
        user_tasks.append(task_info)

    data = {ID: user_tasks}

    with open(f"{ID}.json", 'w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    main()
