from flask import Blueprint, jsonify, request
from services.services import create_exercise, get_all_exercises, get_all_workouts

api = Blueprint('api', __name__)

@api.route('/exercises', methods=['GET'])
def fetch_exercises():
    exercises = get_all_exercises()

    exercises_list = [
        {"id": e.id, "name": e.name} for e in exercises
    ]

    return jsonify(exercises_list)


@api.route('/exercises', methods=['POST'])
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


@api.route('/workouts', methods=['GET'])
def fetch_workouts():
    workouts = get_all_workouts()

    workouts_list = [
        {
            "id": w.id,
            "date": w.date,
            "workout_type": w.workout_type,
            "notes": w.notes
        } for w in workouts
    ]

    return jsonify(workouts_list)