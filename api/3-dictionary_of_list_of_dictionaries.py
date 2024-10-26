#!/usr/bin/python3
"""Script to export all employees TODO list data to JSON format
"""
import json
import requests
import sys


def get_employee(employee_id):
    """Fetches employee data from the API"""
    employee_data = "https://jsonplaceholder.typicode.com/users/"
    employee_request = requests.get(employee_data + str(employee_id))
    return employee_request.json()


def get_todo(employee_id):
    """Fetches TODO list data for an employee from the API"""
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId="
    todo_request = requests.get(todo_url + str(employee_id))
    return todo_request.json()


def export_all_tasks():
    """Exports all employees' TODO list data to JSON file"""
    all_tasks = {}

    for employee_id in range(1, 11):
        try:
            todo_result = get_todo(employee_id)
            employee_result = get_employee(employee_id)
            username = employee_result.get('username')

            task_list = []
            for todo in todo_result:
                task_list.append({
                    "username": username,
                    "task": todo.get('title'),
                    "completed": todo.get('completed')
                })

            all_tasks[str(employee_id)] = task_list

        except requests.RequestException as e:
            print(f"Error fetching data for employee {employee_id}: {e}")
            continue

    with open("todo_all_employees.json", mode='w') as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    export_all_tasks()
