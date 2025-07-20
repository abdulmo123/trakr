from flask import Flask
from models import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def demo():
    return "Workout Tracker API!"

if __name__ == "__main__":
    app.run(debug=True)