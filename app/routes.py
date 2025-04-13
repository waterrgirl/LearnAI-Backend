# app/routes.py
from flask import Blueprint, jsonify, request
from app.firebase_config import db  # Import Firestore client

main = Blueprint("main", __name__)

@main.route('/')
def home():
    return jsonify({"message": "Flask backend with Firebase is running on port 5001!"})

@main.route('/api/add-task', methods=['POST'])
def add_task():
    data = request.get_json()
    # Create a new document with an auto-generated ID
    doc_ref = db.collection('tasks').document()
    task = {
        "title": data["title"],
        "deadline": data.get("deadline"),
        "priority": data.get("priority", "Low"),
        "completed": False
    }
    # Save to Firestore
    doc_ref.set(task)
    task["id"] = doc_ref.id
    return jsonify({"message": "Task added!", "task": task}), 201

@main.route('/api/tasks', methods=['GET'])
def list_tasks():
    tasks = []
    # Retrieve all tasks
    for doc in db.collection('tasks').stream():
        task_data = doc.to_dict()
        task_data["id"] = doc.id
        tasks.append(task_data)
    return jsonify(tasks), 200
