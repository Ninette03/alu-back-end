#!/usr/bin/python3
"""
    Script that exports data in the JSON format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    
    user = json.loads(request_employee.text)
   
    username = user.get("username")
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    tasks = []
    user_todos = json.loads(request_todos.text)
    
    for dictionary in user_todos:
        task = {}
        task["task"] = dictionary.get("title")
        task["completed"] = dictionary.get("completed")
        task["username"] = username
        tasks.append(task)

    with open('{}.json'.format(argv[1]), 'w') as json_file:
        json.dump({argv[1]: tasks}, json_file)