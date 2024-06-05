#!/usr/bin/python3
"""
This module retrieves and displays TODO list progress for a given employee ID
from a REST API.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for an employee.

    Args:
        employee_id (int): The ID of the employee.
    """
    try:
        # Fetch user details
        user_response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        )
        user_response.raise_for_status()  # Raise an error for bad status codes
        user_data = user_response.json()

        # Fetch todo list for the user
        todo_response = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        )
        todo_response.raise_for_status()  # Raise an error for bad status codes
        todos = todo_response.json()

        # Extract user name
        employee_name = user_data.get('name')

        # Calculate total tasks and completed tasks
        total_tasks = len(todos)
        done_tasks = [todo for todo in todos if todo.get('completed')]
        number_of_done_tasks = len(done_tasks)

        # Display results
        print(f"Employee {employee_name} is\
                done with tasks({number_of_done_tasks}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t {task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except ValueError:
        print("Error: Invalid JSON response")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
