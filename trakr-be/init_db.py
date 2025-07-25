from dotenv import load_dotenv
import psycopg2
import argparse
import os 

load_dotenv()

DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')


def connect():
    conn = psycopg2.connect(
        dbname='trakr',
        user=f'{DATABASE_USERNAME}',
        password=f'{DATABASE_PASSWORD}',
        port=5432,
    )

    with conn.cursor() as cur:
        cur.execute('SET search_path TO trakr;')
    conn.commit()
    return conn


def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        create table if not exists trakr.exercises (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        );
    """
    )

    cur.execute("""
        create table if not exists trakr.workouts (
            id SERIAL PRIMARY KEY,
            date DATE NOT NULL,
            workout_type VARCHAR(100),
            notes TEXT
        )
    """
    )

    cur.execute("""
        create table if not exists trakr.workout_exercises (
            id SERIAL PRIMARY KEY,
            workout_id INTEGER NOT NULL REFERENCES trakr.exercises(id) ON DELETE CASCADE,
            exercise_id INTEGER NOT NULL REFERENCES trakr.workouts(id) ON DELETE CASCADE,
            sets INTEGER,
            reps INTEGER,
            weight FLOAT
        );
    """
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Tables CREATED successfully!")


def drop_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("drop table if exists trakr.exercises;")
    cur.execute("drop table if exists trakr.workouts;")
    cur.execute("drop table if exists trakr.workout_exercises;")
    conn.commit()

    cur.close()
    conn.close()
    print("Tables DROPPED successfully!")


def truncate_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("truncate table if exists trakr.exercises;")
    cur.execute("truncate table if exists trakr.workouts;")
    cur.execute("truncate table if exsits trakr.workout_exercises;")
    conn.commit()

    cur.close()
    conn.close()
    print("Tables TRUNCATED successfully!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Database management script")
    parser.add_argument('--create', action='store_true', help='create tables')
    parser.add_argument('--drop', action='store_true', help='drop tables')
    parser.add_argument('--truncate', action='store_true', help='truncate tables')

    args = parser.parse_args()

    if args.create:
        create_tables()
    elif args.drop:
        drop_tables()
    elif args.truncate:
        truncate_tables()
    else:
        print("Argument not provided")