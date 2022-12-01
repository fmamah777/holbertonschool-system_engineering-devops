#!/usr/bin/python3
"""Uses a REST API to retrieve information,
for a given employee ID, returns information about
his/her TODO list progress."""
from os import sys
import requests


if __name__ == "__main__":
    user_id = sys.argv[1]
    id = int(user_id)
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(id))
    name = user.json().get("name")
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    all = 0
    complete = 0

    for k in todos.json():
        if k.get('userId') is id:
            all += 1
        if k.get('userId') is id and k.get('completed') is True:
            complete += 1

    print("Employee {} is done with tasks({}/{}):".format(name, complete, all))

    for k in todos.json():
        if k.get('userId') is id and k.get('completed') is True:
            print("\t {}".format(k.get('title')))
