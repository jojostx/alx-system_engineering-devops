#!/usr/bin/python3
""" Python script that, queries a  REST API, for a given employee ID,
returns information about their TODO list progress """
import csv
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    u_id = sys.argv[1]
    csv_path = f"{u_id}.csv"

    res = requests.get(f"{url}users/{u_id}")
    user_o = res.json()

    res = requests.get(f"{url}todos?userId={u_id}")
    tasks = res.json()

    name = user_o.get('username')

    l_task = []
    for task in tasks:
        l_task.append([u_id, name, task.get('completed'), task.get('title')])

    with open(csv_path, 'w') as f:
        writer = csv.writer(f,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in l_task:
            writer.writerow(task)
