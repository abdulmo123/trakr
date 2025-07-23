from models import Exercise, db

def get_all_exercises():
    return Exercise.query.all()


def create_exercise(name):
    new_exercise=Exercise(name=name)
    db.session.add(new_exercise)
    db.session.commit()

    return new_exercise