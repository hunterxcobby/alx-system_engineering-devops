#!/usr/bin/python3

"""
Script to retrieve and display TODO list progress for a given employee
using a REST API.

Requirements:
- Use urllib or requests module
- Accept an integer as a parameter (employee ID)
- Display progress information in the specified format
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """ Fetches and displays TODO list progress for a given employee.

    Args:
    - employee_id (int): ID of the employee to retrieve TODO list for.

    Returns:
    - None
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch TODO list for the employee
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = sum(task.get("completed", False) for task in todos_data)

    # Display progress information
    print("Employee {} is done with tasks ({}/{}):".format(
        employee_name, completed_tasks, total_tasks), end='\n')
    # print("{}: {} completed tasks out of {}".format(
    # employee_name, completed_tasks, total_tasks))

    # Display titles of completed tasks
    for task in todos_data:
        if task.get('completed', False):
            print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Extract employee ID from command-line arguments
    employee_id = int(sys.argv[1])

    # Call the function to get and display TODO list progress
    get_employee_todo_progress(employee_id)
