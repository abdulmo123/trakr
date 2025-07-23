from flask import Flask
from models import db
from config import Config
from routes.routes import api

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def demo():
    return "Workout Tracker API!"

if __name__ == "__main__":
    app.run(debug=True)