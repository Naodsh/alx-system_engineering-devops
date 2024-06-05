#!/usr/bin/python3
"""
This module retrieves TODO list progress for a given employee ID
from a REST API and exports the data to a JSON file.
"""
import json
import requests
import sys


def export_to_json(employee_id):
    """
    Fetches TODO list progress for an employee and exports it to a JSON file.

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

        # Extract user details
        user_id = user_data.get('id')
        username = user_data.get('username')

        # Prepare data for JSON export
        tasks = [{
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
        } for todo in todos]

        data = {str(user_id): tasks}

        # Write data to JSON file
        file_name = f"{user_id}.json"
        with open(file_name, 'w') as json_file:
            json.dump(data, json_file)

        print(f"Data exported to {file_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except ValueError:
        print("Error: Invalid JSON response")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_json(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
