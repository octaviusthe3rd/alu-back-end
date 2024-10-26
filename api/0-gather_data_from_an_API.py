#!/usr/bin/python3
"""
A script that uses JSONPlaceholder API to get information about employee TODO list
progress
"""
import requests
import sys


def get_employee(employee_id):
    """Fetches employee data from JSONPlaceholder API"""
    employee_data = "https://jsonplaceholder.typicode.com/users/"
    employee_request = requests.get(employee_data + str(employee_id))
    return employee_request.json()


def get_todo(employee_id):
    """Fetches TODO list data for an employee from JSONPlaceholder API"""
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId="
    todo_request = requests.get(todo_url + str(employee_id))
    return todo_request.json()


def todo_tasks(todo_result):
    """Calculates the number of completed tasks vs total tasks"""
    completed_tasks = 0
    total_tasks = len(todo_result)
    for todo in todo_result:
        if todo.get('completed'):
            completed_tasks += 1
    return f"({completed_tasks}/{total_tasks})"


def todo_titles(todo_result):
    """Prints the titles of completed TODO list items"""
    for todo in todo_result:
        if todo.get('completed'):
            print(f"     {todo.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an employee ID as argument")
        sys.exit(1)

    try:
        employee_id = sys.argv[1]
        todo_result = get_todo(employee_id)
        employee_result = get_employee(employee_id)
        print(f"Employee {employee_result.get('name')} is done with tasks"
              f"{todo_tasks(todo_result)}:")
        todo_titles(todo_result)
    except requests.RequestException as e:
        print(f"Error making request: {e}")
