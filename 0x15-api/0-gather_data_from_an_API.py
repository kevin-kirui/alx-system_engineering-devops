#!/usr/bin/python3
"""
Script to gather data from a REST API about an employee's TODO list progress.
"""

import sys
import requests

def fetch_todo_list(employee_id):
    """
    Fetches the TODO list for the given employee ID from the API.
    """
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)
    response = requests.get(url)
    return response.json()

def display_progress(employee_id, todo_list):
    """
    Displays the progress of the employee's TODO list.
    """
    employee_name = todo_list[0]['username']
    total_tasks = len(todo_list)
    completed_tasks = sum(1 for task in todo_list if task['completed'])

    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))

    for task in todo_list:
        if task['completed']:
            print("\t", task['title'])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    todo_list = fetch_todo_list(employee_id)
    display_progress(employee_id, todo_list)

