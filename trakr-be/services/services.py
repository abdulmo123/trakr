from models import Exercise, db, Workout
from sqlalchemy import text

def get_all_exercises():
    return Exercise.query.all()


def create_exercise(name):
    new_exercise=Exercise(name=name)
    db.session.add(new_exercise)
    db.session.commit()

    return new_exercise


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
        RETURNING id
    """
    )

    result = db.session.execute(insert_sql, {
        "date": date,
        "workout_type": workout_type,
        "notes": notes
    })

    row = result.fetchone()
    new_id = row[0] if row else None

    db.session.commit()
    return new_id