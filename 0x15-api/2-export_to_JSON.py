#!/usr/bin/python3
"""
Script that uses JSONPlaceholder API to get information about an employee
and exports TODO list to JSON.

Requirements:
- Records all tasks that are owned by this employee
- Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
- File name must be: USER_ID.json
"""

import json
import requests
import sys


def get_employee_info_and_tasks(employee_id):
    """
    Fetches information about an employee and their tasks from
    JSONPlaceholder API and exports TODO list to JSON.

    Args:
    - employee_id (str): ID of the employee to retrieve information for.

    Returns:
    - None
    """
    # JSONPlaceholder API base URL
    api_url = 'https://jsonplaceholder.typicode.com/'

    # Construct URLs for user and tasks
    user_url = '{}users/{}'.format(api_url, employee_id)
    todos_url = '{}todos?userId={}'.format(api_url, employee_id)

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Extract username
    username = user_data.get('username')

    # Fetch tasks for the employee
    todos_response = requests.get(todos_url)
    tasks_data = todos_response.json()

    # Create a list of tasks with relevant information
    tasks_list = []
    for task in tasks_data:
        dict_task = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        }
        tasks_list.append(dict_task)

    # Create a dictionary with the employee's tasks
    employee_tasks = {str(employee_id): tasks_list}

    # Create a JSON file with the employee's tasks
    filename = '{}.json'.format(employee_id)
    with open(filename, mode='w') as json_file:
        json.dump(employee_tasks, json_file)


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    # Extract employee ID from command-line arguments
    employee_id = sys.argv[1]

    # Call the function to get employee information and tasks,
    # and create a JSON file
    get_employee_info_and_tasks(employee_id)
