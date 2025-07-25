from flask import Blueprint, jsonify, request
from services.services import create_exercise, get_all_exercises, get_all_workouts, insert_workout, log_workout_exercises
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

@api.route('/workouts', methods=['POST'])
def insert_workouts():
    data = request.get_json()
    date = data.get('date')
    workout_type = data.get('workout_type')
    notes = data.get('notes')

    if not date:
        return jsonify({
            "error": "Date of workout not given!"
        }), 400

    workout = insert_workout(date, workout_type, notes)
    return jsonify({
        "date": workout.date,
        "workout_type": workout.workout_type,
        "notes": workout.notes
    }), 201

@api.route("/workout_exercises", methods=["POST"])
def log_workout_exercises():
    data = request.get_json()
    workout_id = data.get('workout_id')
    exercise_id = data.get('exercise_id')
    sets = data.get('sets')
    reps = data.get('reps')
    weight = data.get('weight')

    if not workout_id or exercise_id:
        return jsonify({
            "error": "Workout and/or Exercise not given!"
        })
    
    workout_exercise = log_workout_exercises(
        workout_id, exercise_id, sets, reps, weight
    )

    return jsonify({
        "workout_id": workout_exercise.workout_id,
        "exercise_id": workout_exercise.exercise_id,
        "sets": workout_exercise.sets,
        "reps": workout_exercise.reps,
        "weight": workout_exercise.weight
    })