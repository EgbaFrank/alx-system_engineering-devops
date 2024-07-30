#!/usr/bin/python3
"""
Returns information on a given employee
"""
import csv
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

    name = fetch_data(user_url).get("username")
    todos = fetch_data(todo_url)

    for task in todos:
        task.pop('id')
        task['username'] = name

    fieldnames = ["userId", "username", "completed", "title"]

    with open(f'{ID}.csv', mode='w', newline='') as file:
        csv_writer = csv.DictWriter(
                file,
                fieldnames=fieldnames,
                quoting=csv.QUOTE_ALL
                )
        csv_writer.writerows(todos)
