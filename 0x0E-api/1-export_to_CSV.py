#!/usr/bin/python3
""" REST API to request information"""
import csv
from os import sys
import requests


if __name__ == "__main__":
    try:
        user_id = sys.argv[1]
        id = int(user_id)

    except ValueError:
        print("ID not INT")

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(id))
    name = user.json()["name"]
    username = user.json()["username"]
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    file = user_id + ".csv"

    with open(file, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for k in todos.json():
            if k['userId'] == id:
                data = [k['userId'], username, k['completed'], k['title']]
                writer.writerow(data)
