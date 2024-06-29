#!/usr/bin/python3
"""Gather data from an API"""

import json
import requests
import sys

if __name__ == "__main__":
    # Check if an employee ID was provided
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    # Get the employee ID from the command line argument
    employee_id = sys.argv[1]

    # Fetch user information
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_response = requests.get(user_url)
    user = user_response.json()

    # Fetch TODO list
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Filter completed tasks
    done_tasks = [task for task in todos if task['completed']]

    # Print the TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(
        user['name'],
        len(done_tasks),
        len(todos)
    ))

    # Print the titles of completed tasks
    for task in done_tasks:
        print("\t {}".format(task['title']))
