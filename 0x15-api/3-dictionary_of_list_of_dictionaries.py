#!/usr/bin/python3
""" Python script that, queries a REST API, for all the employee's todos,
and exports the data in JSON format to file. """
import json
import requests

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    json_path = f"todo_all_employees.json"
    d_tasks = {}

    res = requests.get(f"{url}users")
    users = res.json()

    for user in users:
        u_id = user.get('id')
        res = requests.get(f"{url}todos?userId={u_id}")
        tasks = res.json()
        name = user.get('username')

        l_task = []
        for task in tasks:
            task_dict = {
                "username": name,
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            l_task.append(task_dict)

        d_tasks[str(u_id)] = l_task

    with open(json_path, 'w') as f:
        json.dump(d_tasks, f)
