#!/usr/bin/python3
""" Exports a list of data for each user into a json file """
import json
from os import sys
import requests


if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users")
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    file = "todo_all_employees.json"

    with open(file, 'w') as f:
        Dict = {}
        for person in user.json():
            id = person['id']
            Dict[id] = []
            for k in todos.json():
                if k['userId'] == id:
                    dictionary = {"username": person['username'],
                                  "task": k['title'],
                                  "completed": k['completed']}
                    Dict[id].append(dictionary)
        json.dump(Dict, f)
