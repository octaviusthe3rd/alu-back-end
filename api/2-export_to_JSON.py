#!/usr/bin/python3
"""Script to export TODO list data to JSON format
"""
import json
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


def export_to_json(employeeId, username, todoList):
    """Exports TODO list data to JSON file"""
    taskList = []
    for todo in todoList:
        taskList.append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
        }) 
    jsonData = {employeeId: taskList}
    fileName = f"{employeeId}.json"    
    with open(fileName, mode='w') as json_file:
        json.dump(jsonData, json_file)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an employee ID as argument")
        sys.exit(1)
    try:
        employeeId = sys.argv[1]
        todoResult = getTodo(employeeId)
        employeeResult = getEmployee(employeeId)
        username = employeeResult.get('username')
        export_to_json(employeeId, username, todoResult)
    except requests.RequestException as e:
        print(f"Error making request: {e}")
