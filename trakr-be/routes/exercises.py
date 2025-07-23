from flask import Blueprint, jsonify, request
from services.services import create_exercise, get_all_exercises

exercises_bp = Blueprint('exercises', __name__)

@exercises_bp.route('/exercises', methods=['GET'])
def fetch_exercises():
    exercises = get_all_exercises()

    exercises_list = [
        {"id": e.id, "name": e.name} for e in exercises
    ]

    return jsonify(exercises_list)


@exercises_bp.route('/exercises', methods=['POST'])
def add_exercise():
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({
            "error": "Exercise name not given!"
        }), 400
    
    exercise = create_exercise(name)
    return jsonify({
        "id": exercise.id,
        "name": exercise.name
    }), 201