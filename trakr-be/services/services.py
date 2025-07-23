from models import Exercise, db, Workout

def get_all_exercises():
    return Exercise.query.all()


def create_exercise(name):
    new_exercise=Exercise(name=name)
    db.session.add(new_exercise)
    db.session.commit()

    return new_exercise


def get_all_workouts():
    return Workout.query.all()