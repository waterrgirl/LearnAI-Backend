# app/routes.py
from flask import Blueprint, jsonify, request
from app.firebase_config import db  # Firestore client

main = Blueprint("main", __name__)

@main.route('/')
def home():
    return jsonify({"message": "Flask backend with Firebase is running on port 5001!"})

@main.route('/api/tasks', methods=['GET'])
def list_tasks():
    tasks = []
    for doc in db.collection('tasks').stream():
        data = doc.to_dict()
        data["id"] = doc.id
        tasks.append(data)
    return jsonify(tasks), 200

@main.route('/api/add-task', methods=['POST'])
def add_task():
    data = request.get_json()
    doc_ref = db.collection('tasks').document()
    task = {
        "title": data["title"],
        "deadline": data.get("deadline"),
        "priority": data.get("priority", "Low"),
        "completed": False
    }
    doc_ref.set(task)
    task["id"] = doc_ref.id
    return jsonify({"message": "Task added!", "task": task}), 201

@main.route('/api/tasks/<task_id>', methods=['PATCH'])
def update_task(task_id):
    data = request.get_json()
    if 'completed' not in data:
        return jsonify({"error": "Nothing to update"}), 400

    db.collection('tasks').document(task_id).update({
        'completed': data['completed']
    })
    return jsonify({"message": "Task updated!"}), 200

@main.route('/api/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    db.collection('tasks').document(task_id).delete()
    return jsonify({"message": "Task deleted!"}), 200
