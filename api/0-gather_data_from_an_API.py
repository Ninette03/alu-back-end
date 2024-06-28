#!/usr/bin/python3

import requests
import json
import sys
if __name__ == "__main__":
    USER_URL = 'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1])
    res = requests.get(USER_URL)
    user = json.loads(res.text)
    num = sys.argv[1]
    TODO_URL = 'https://jsonplaceholder.typicode.com/todos'.format(num)
    res = requests.get(TODO_URL)
    todos = json.loads(res.text)
    completed_tasks =[]

    todo_counter = 0
    completed_counter = 0
    
    for i in todos:
        if i['completed']:
            completed_tasks.append(i)
    print("Employee {} is done with tasks({}/{}):"format(
        user['name'],
        len(completed_tasks),
        len(todos)))
    for i in completed_tasks:
        print("\t {}".format(i["title"]))