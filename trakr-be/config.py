import os 

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://username:password@localhost:5432/workout_tracker')
    SQLALCHEMY_TRACK_MODIFICATIONS = False