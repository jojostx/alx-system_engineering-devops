#!/usr/bin/python3
""" Python script that, queries a REST API, for a given employee ID,
exports information about their TODO list progress in JSON format to file. """
import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    u_id = sys.argv[1]
    json_path = f"{u_id}.json"

    res = requests.get(f"{url}users/{u_id}")
    user_o = res.json()

    res = requests.get(f"{url}todos?userId={u_id}")
    tasks = res.json()

    name = user_o.get('username')

    l_task = []
    for task in tasks:
        task_dict = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": name
        }
        l_task.append(task_dict)

    d_task = {str(u_id): l_task}

    with open(json_path, 'w') as f:
        json.dump(d_task, f)
