#!/usr/bin/python3
import requests
import json

USER_ID = 1
USER_URL = f'https://jsonplaceholder.typicode.com/users/${USER_ID}'
TODO_URL = f'https://jsonplaceholder.typicode.com/todos'

employee = requests.get(USER_URL).json()
todos = requests.get(TODO_URL).json()

todo_counter = 0
completed_counter = 0
completed_tasks =[]
for todo in todos:
    if todo['userId'] == USER_ID:
        todo_counter += 1
        if todo['completed'] is True:
            completed_counter += 1
            completed_tasks.append(todo['title'])

employee_name = employee['name']
print(f"Employee {employee_name} is done with tasks({completed_counter}/{todo_counter})")
for title in completed_tasks:
    print(title)