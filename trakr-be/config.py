from dotenv import load_dotenv
import os 

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret-key')
    DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

    if not DATABASE_USERNAME or not DATABASE_PASSWORD:
        raise ValueError("Missing DATABASE_USERNAME or DATABASE_PASSWORD environment variables")

    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@localhost:5432/trakr"
    SQLALCHEMY_TRACK_MODIFICATIONS = False