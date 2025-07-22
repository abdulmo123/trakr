from models import Exercise

def get_all_exercises():
    return Exercise.query.all()

