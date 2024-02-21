#!/usr/bin/python3

"""
Script that uses JSONPlaceholder API to get information about an employee
and exports TODO list to CSV.

Requirements:
- Records all tasks that are owned by this employee
- Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name must be: USER_ID.csv
"""

import csv
import requests
import sys


def get_employee_info_and_tasks(employee_id):
    """
    Fetches information about an employee and their tasks from
    JSONPlaceholder API.

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
        tasks_list.append(
            [employee_id, username, task.get('completed'), task.get('title')])

    # Create a CSV file with the employee's tasks
    filename = '{}.csv'.format(employee_id)
    with open(filename, mode='w') as employee_file:
        employee_writer = csv.writer(
            employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        # Write header
        # employee_writer.writerow(
        # ['EmployeeID', 'Username', 'Completed', 'Title'])

        # Write tasks data
        for task in tasks_list:
            employee_writer.writerow(task)


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    # Extract employee ID from command-line arguments
    employee_id = sys.argv[1]

    # Call the function to get employee information and tasks,
    # and create a CSV file
    get_employee_info_and_tasks(employee_id)
