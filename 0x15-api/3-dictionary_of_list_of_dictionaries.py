#!/usr/bin/python3
"""
Script that uses JSONPlaceholder API to get information about ALL employees
and exports their TODO lists to a single JSON file.

Requirements:
- Records all tasks for each employee
- Format must be: { "USER_ID": [{"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, ...], ... }
- File name must be: todo_all_employees.json
"""

import json
import requests
import sys


def get_all_employees_and_tasks():
    """
    Fetches information about all employees and their tasks from
    JSONPlaceholder API
    and exports TODO lists to a single JSON file.

    Args:
    - None

    Returns:
    - None
    """
    # JSONPlaceholder API base URL
    api_url = 'https://jsonplaceholder.typicode.com/'

    # Fetch information about all users
    users_url = '{}users'.format(api_url)
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Dictionary to store tasks for all employees
    all_employees_tasks = {}

    # Iterate through each user
    for user in users_data:
        name = user.get('username')
        userid = user.get('id')

        # Fetch tasks for the current employee
        todos_url = '{}todos?userId={}'.format(api_url, userid)
        todos_response = requests.get(todos_url)
        tasks_data = todos_response.json()

        # List to store tasks for the current employee
        tasks_list = []

        # Iterate through each task for the current employee
        for task in tasks_data:
            dict_task = {
                "username": name,
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            tasks_list.append(dict_task)

        # Add tasks for the current employee to the dictionary
        all_employees_tasks[str(userid)] = tasks_list

    # Create a JSON file with tasks for all employees
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as json_file:
        json.dump(all_employees_tasks, json_file)


if __name__ == "__main__":
    # Call the function to get information about all employees and their tasks,
    # and create a JSON file
    get_all_employees_and_tasks()
