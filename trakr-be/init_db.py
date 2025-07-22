# from dotenv import load_dotenv
import psycopg2
import os 

# load_dotenv()

DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

def create_tables():
    conn = psycopg2.connect(
        dbname='trakr',
        user=f'{DATABASE_USERNAME}',
        password=f'{DATABASE_PASSWORD}',
        port=5432
    )

    cur = conn.cursor()

    create_exercises_table = """
        create table if not exists exercises (
            id serial primary key,
            name varchar(100) not null
        );
    """

    cur.execute(create_exercises_table)
    conn.commit()

    cur.close()
    conn.close()
    print("Tables created successfully!")

if __name__ == '__main__':
    create_tables()