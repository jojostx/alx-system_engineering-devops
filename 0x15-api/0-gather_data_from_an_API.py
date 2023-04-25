#!/usr/bin/python3
""" queries JSONPlaceholder API to get information about employee """
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    userId = sys.argv[1]
    res = requests.get(f"{url}users/{userId}")
    json_o = res.json()
    name = json_o.get('name')

    print(f"Employee {name} is done with tasks", end="")

    res = requests.get(f"{url}todos?userId={userId}")
    tasks = res.json()

    l_task = []
    for task in tasks:
        if task.get('completed') is True:
            l_task.append(task)

    print("({}/{}):".format(len(l_task), len(tasks)))
    for task in l_task:
        print("\t {}".format(task.get("title")))
