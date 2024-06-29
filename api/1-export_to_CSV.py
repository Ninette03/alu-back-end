#!/usr/bin/python3
"""
    Script that exports data in the CSV format
"""
import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    
    user = json.loads(request_employee.text)
    username = user.get("username")
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))
  
    tasks = {}
    user_todos = json.loads(request_todos.text)
    for dictionary in user_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    with open('{}.csv'.format(argv[1]), mode='w', newline='') as file:
        file_editor = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for k, v in tasks.items():
            file_editor.writerow([argv[1], username, v, k])

    print('Data exported to {}.csv'.format(argv[1]))