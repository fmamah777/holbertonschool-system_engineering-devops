#!/usr/bin/python3
"""
This example will take the employees id number
and return the amount of tasks done vs the total
amount of tasks also listing what takss are done.
This then exports the data for users into a json file.
"""

import json
import requests
import sys


if __name__ == '__main__':
    # check for valid input, argument passed must be type int #
    if sys.argv[1].isdigit():

        # assigned to variables #
        user_id = sys.argv[1]
        employee = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}"
            .format(user_id)).json()
        to_do = requests.get(
            "https://jsonplaceholder.typicode.com/todos/?userId={}"
            .format(user_id)).json()
        completed = []
        for done in to_do:
            if done.get("completed") is True:
                completed.append(done.get("title"))

        # print requested outputs #
        print("Employee {} is done with tasks ({}/{}):".format(
            employee.get("name"), len(completed), len(to_do)))
        for title in completed:
            print("\t {}".format(title))

        # export data to json file #
        with open("{}.json".format(user_id), 'w') as file:
            task_dict = {user_id: [{
                'task': task.get('title'),
                'username': employee.get('username'),
                'completed': task.get('completed')
            } for task in to_do]}
            json.dump(task_dict, file)
