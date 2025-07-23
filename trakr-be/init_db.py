from dotenv import load_dotenv
import psycopg2
import argparse
import os 

load_dotenv()

DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')


def connect():
    return psycopg2.connect(
        dbname='trakr',
        user=f'{DATABASE_USERNAME}',
        password=f'{DATABASE_PASSWORD}',
        port=5432
    )


def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        create table if not exists exercises (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        );
    """
    )

    cur.execute("""
        create table if not exists workouts (
            id SERIAL PRIMARY KEY,
            date DATE NOT NULL,
            workout_type VARCHAR(100),
            notes TEXT
        )
    """
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Tables CREATED successfully!")


def drop_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("drop table if exists exercises;")
    conn.commit()

    cur.close()
    conn.close()
    print("Tables DROPPED successfully!")


def truncate_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("truncate table if exists exercises;")
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