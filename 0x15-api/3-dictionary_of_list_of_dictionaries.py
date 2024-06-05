#!/usr/bin/python3
import requests
import json

# Define the URLs for users and tasks
users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"

# Fetch the data
users_response = requests.get(users_url)
todos_response = requests.get(todos_url)

# Check if the requests were successful
if users_response.status_code == 200 and todos_response.status_code == 200:
    users = users_response.json()
    todos = todos_response.json()

    # Create a dictionary to hold the data
    all_tasks = {}

    # Populate the dictionary with user tasks
    for user in users:
        user_id = user["id"]
        username = user["username"]

        # Filter todos for the current user
        user_todos = [todo for todo in todos if todo["userId"] == user_id]

        # Create the list of tasks for the user
        tasks_list = []
        for todo in user_todos:
            task = {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            tasks_list.append(task)

        # Add the tasks list to the all_tasks dictionary
        all_tasks[user_id] = tasks_list

    # Write the data to a JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)
else:
    print("Failed to fetch data from API.")
