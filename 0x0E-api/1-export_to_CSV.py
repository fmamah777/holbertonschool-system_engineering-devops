#!/usr/bin/python3
"""
This example will take the employees id number 
and return the amount of tasks done vs the total
amount of tasks also listing what taks are done then it saves the
task information for that user into a .csv file.
"""
import csv
import requests
import sys


if __name__ == '__main__':
    # check for valid input, argument must be type int #
    if sys.argv[1].isdigit():

        # assign values to variables #
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

        # requested outputs #
        print("Employee {} is done with tasks({}/{}):".format(
            employee.get("name"), len(completed), len(to_do)))
        for title in completed:
            print("\t {}".format(title))

        # request from values to CSV format file #
        with open("{}.csv".format(user_id), 'w') as file:
            csv_write = csv.writer(file, quoting=csv.QUOTE_ALL)
            for item in to_do:
                csv_write.writerow([
                    user_id, employee.get("username"),
                    item.get("completed"), item.get("title")])
