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
        sys.exit(2)
    return response.json()


def main():
    """Main function to save all employee's info to a JSON file"""
    if len(sys.argv) != 1:
        print(f"Usage: {sys.argv[0]}")
        sys.exit(1)

    todo_url = f"https://jsonplaceholder.typicode.com/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users"

    users = fetch_data(user_url)
    todo_data = fetch_data(todo_url)

    if not users:
        print(f"No user data found")
        sys.exit(3)

    data = {}
    for user_data in users:
        username = user_data.get('username')
        ID = user_data.get('id')

        if not username:
            print(f"User with ID {ID} does not have a username.")
            sys.exit(4)

        user_tasks = []

        for task in todo_data:
            if task.get('userId') == ID:
                task_info = {
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                }
                user_tasks.append(task_info)

        data.update({ID: user_tasks})

    with open("todo_all_employees.json", 'w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    main()
