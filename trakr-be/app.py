from flask import Flask
from models import db
from config import Config
from routes.exercises import exercises_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(exercises_bp, url_prefix='/api')

@app.route('/')
def demo():
    return "Workout Tracker API!"

if __name__ == "__main__":
    app.run(debug=True)