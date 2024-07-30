#!/usr/bin/python3
"""
Returns information on a given employee
"""
import requests
import sys


def fetch_data(url):
    """Fetches data from URL"""
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data from {url}")
        sys.exit(3)
    return response.json()


if __name__ == "__main__":
    """Prints an employee's info"""
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} [ID]")
        sys.exit(1)

    try:
        ID = int(sys.argv[1])
        todo_url = f"https://jsonplaceholder.typicode.com/users/{ID}/todos"
        user_url = f"https://jsonplaceholder.typicode.com/users/{ID}"
    except ValueError:
        print("Invalid ID")
        sys.exit(2)

    name = fetch_data(user_url).get("name")
    todos = fetch_data(todo_url)

    task_done = sum(1 for task in todos if task.get("completed"))

    print(f"Employee {name} is done with tasks({task_done}/{len(todos)}):")
    for task in todos:
        if task.get("completed"):
            print(f"\t {task.get('title')}")
