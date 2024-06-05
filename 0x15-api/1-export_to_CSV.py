#!/usr/bin/python3
"""
This module retrieves TODO list progress for a given employee
ID from a REST API and exports the data to a CSV file.
"""
import csv
import requests
import sys


def export_to_csv(employee_id):
    """
    Fetches TODO list progress for an employee and exports it to a CSV file.

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

        # Create CSV file
        file_name = f"{user_id}.csv"
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for task in todos:
                writer.writerow([
                    user_id,
                    username,
                    task.get('completed'),
                    task.get('title')
                ])

        print(f"Data exported to {file_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except ValueError:
        print("Error: Invalid JSON response")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_csv(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
