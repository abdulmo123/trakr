from flask import Blueprint, jsonify
from services.services import get_all_exercises

exercises_bp = Blueprint('exercises', __name__)

@exercises_bp.route('/exercises', methods=['GET'])
def fetch_exercises():
    exercises = get_all_exercises()

    exercises_list = [
        {"id": e.id, "name": e.name} for e in exercises
    ]

    return jsonify(exercises_list)