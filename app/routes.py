# app/routes.py
from flask import Blueprint, jsonify, request

# Create a Blueprint named 'main'
main = Blueprint("main", __name__)

# An in-memory list to store tasks (replace with a database in a real app)
tasks = []

@main.route('/')
def home():
    return jsonify({"message": "Flask backend is running on VS Code with port 5001!"})

@main.route('/add-task', methods=['POST'])
def add_task():
    data = request.get_json()
    task = {
        "id": len(tasks) + 1,
        "title": data.get("title"),
        "deadline": data.get("deadline"),
        "priority": data.get("priority", "Low"),
        "completed": False
    }
    tasks.append(task)
    return jsonify({"message": "Task added successfully!", "task": task}), 201
