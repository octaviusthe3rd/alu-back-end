#!/usr/bin/env python3
import requests
import sys

def getTodo(employeeID):
    todoUrl = "https://jsonplaceholder.typicode.com/todos?userId="
    todoRequest = requests.get(todoUrl + str(employeeID))
    return todoRequest.json()

def getEmployees(employeeID):
    employeeData = "https://jsonplaceholder.typicode.com/users/"
    employeeRequest = requests.get(employeeData + str(employeeID))
    return employeeRequest.json()

def todoTasks(todoResult):
    completedTasks = 0
    totalTasks = len(todoResult)

    for todo in todoResult:
        if todo['completed']:
            completedTasks += 1

    return f"{completedTasks}/{totalTasks}"

def todoTitles(todoResult):
    for todo in todoResult:
        if todo['completed']:
            print(f"     {todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an employee ID as argument")
        sys.exit(1)
    
    try:
        employeeID = sys.argv[1]
        todoResult = getTodo(employeeID)
        employeeResult = getEmployees(employeeID)

        print(f"Employee {employeeResult['name']} is done with tasks {todoTasks(todoResult)}:")
        todoTitles(todoResult)

    except requests.RequestException as error:
        print(f"Error making request: {error}")
