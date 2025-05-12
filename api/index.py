from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app, resources={r"/api": {"origins": "*"}})  # Enable CORS for /api endpoint

# Load marks.json from the project root
with open(os.path.join(os.path.dirname(__file__), '..', 'q-vercel-python.json'), 'r') as f:
    marks_data = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    # Get list of names from query parameters
    names = request.args.getlist('name')
    if not names:
        return jsonify({"error": "At least one name is required"}), 400

    # Fetch marks in the order of names provided
    result = []
    for name in names:
        # Search for the student in marks_data
        student = next((item for item in marks_data if item["name"] == name), None)
        if student:
            result.append(student["marks"])
        else:
            return jsonify({"error": f"Student {name} not found"}), 404

    return jsonify({"marks": result}), 200