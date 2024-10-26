#!/usr/bin/python3
"""Script to export TODO list data to CSV format
"""
import csv
import requests
import sys


def getEmployee(employeeId):
    """Fetches employee data from the API"""
    employeeData = "https://jsonplaceholder.typicode.com/users/"
    employeeRequest = requests.get(employeeData + str(employeeId))
    return employeeRequest.json()


def getTodo(employeeId):
    """Fetches TODO list data for an employee from the API"""
    todoUrl = "https://jsonplaceholder.typicode.com/todos?userId="
    todoRequest = requests.get(todoUrl + str(employeeId))
    return todoRequest.json()


def export_to_csv(employeeId, username, todoList):
    """Exports TODO list data to CSV files"""
    fileName = f"{employeeId}.csv"
    with open(fileName, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todoList:
            writer.writerow([
                employeeId,
                username,
                todo.get('completed'),
                todo.get('title')
            ])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an employee ID as argument")
        sys.exit(1)
    try:
        employeeId = sys.argv[1]
        todoResult = getTodo(employeeId)
        employeeResult = getEmployee(employeeId)
        username = employeeResult.get('username')
        export_to_csv(employeeId, username, todoResult)
    except requests.RequestException as e:
        print(f"Error making request: {e}")
