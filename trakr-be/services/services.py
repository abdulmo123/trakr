from models import Exercise, db, Workout
from sqlalchemy import text

def get_all_exercises():
    fetch_sql = text("""
        select * from trakr.exercises
    """
    )

    result = db.session.execute(fetch_sql)
    exercises = result.fetchall()

    return exercises


def create_exercise(name):
    insert_sql = text("""
        insert into trakr.exercises (name)
        values (:name)
        RETURNING id, name
    """
    )

    result = db.session.execute(insert_sql, {
        "name": name
    })

    row = result.fetchone()
    db.session.commit()

    return row


def get_all_workouts():
    fetch_sql = text("""
        select * from trakr.workouts
    """)

    result = db.session.execute(fetch_sql)
    workouts = result.fetchall()

    return workouts

def insert_workout(date, workout_type, notes):
    insert_sql = text("""
        insert into trakr.workouts (date, workout_type, notes)
        values (:date, :workout_type, :notes)
        RETURNING id, date, workout_type, notes
    """
    )

    result = db.session.execute(insert_sql, {
        "date": date,
        "workout_type": workout_type,
        "notes": notes
    })

    row = result.fetchone()
    db.session.commit()

    return row

def log_workout_exercises(workout_id, exercise_id, sets, reps, weight):
    insert_sql = text("""
        INSERT INTO trakr.workout_exercises (workout_id, exercise_id, sets, reps, weight)
        values(:workout_id, :exercise_id, :sets, :reps, :weight)
        RETURNING id, workout_id, exercise_id, sets, reps, weight
    """
    )

    result = db.session.execute(insert_sql, {
        "workout_id": workout_id,
        "exercise_id": exercise_id,
        "sets": sets,
        "reps": reps,
        "weight": weight
    })

    row = result.fetchone()
    db.session.commit()

    return row