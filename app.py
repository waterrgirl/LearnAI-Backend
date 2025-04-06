from flask import Flask, jsonify, request
from flask_cors import CORS
from pyngrok import ngrok

# Set your ngrok authtoken (optional, only if you need to expose your local server publicly)
ngrok.set_auth_token("2uarnvaygW75bBBGIEMG3ZOPqB2_ChDfLvvQHhBzoAQpfptp")

app = Flask(__name__)
CORS(app)

# Open a public URL for the Flask server on port 5001
public_url = ngrok.connect(5001).public_url
print(f"Public URL: {public_url}")

@app.route('/')
def home():
    return jsonify({"message": "Flask backend is running on VS Code with port 5001!"})

# Example API to add a task
tasks = []

@app.route('/add-task', methods=['POST'])
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
