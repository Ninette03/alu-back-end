#!/usr/bin/python3
import requests

USER_ID = 1
USER_URL = f"https://jsonplaceholder.typicode.com/users/${USER_ID}"
TODO_URL = f"https://jsonplaceholder.typicode.com/todos"

employee = requests.get(USER_URL).json()
todos = requests.get(TODO_URL).json()

todo_counter = 0
completed_counter = 0
for todo in todos:
    if todo['userId'] == 1:
        todo_counter += 1
        if todo['completed'] is True:
            completed_counter += 1

print(employee['name'])
print(todo_counter)
print(completed_counter)



