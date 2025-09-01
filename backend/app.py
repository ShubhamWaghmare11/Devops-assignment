from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import time
app = Flask(__name__)
import logging
from logging.handlers import RotatingFileHandler

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# DB_HOST = os.getenv("DB_HOST", "localhost")
# DB_PORT = os.getenv("DB_PORT", "5432")
# DB_NAME = os.getenv("DB_NAME", "mydatabase")
# DB_USER = os.getenv("DB_USER", "myuser")
# DB_PASSWORD = os.getenv("DB_PASSWORD", "mypassword")


DB_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

log_dir = "/shared/logs"
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, "app.log")

file_handler = RotatingFileHandler(log_file, maxBytes=1_000_000, backupCount=3)
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.propagate = True


db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

def wait_for_db():
    retries = 5
    while retries:
        try:
            db.session.execute("SELECT 1")
            return
        except:
            print("Waiting for DB to be ready...")
            time.sleep(3)
            retries -= 1


def seed_users():
    if User.query.count() == 0:
        db.session.add_all([
            User(name='Shubham'),
            User(name='Megha'),
            User(name='Gaurav'),
            User(name='Divij'),
        ])
        db.session.commit()


@app.route("/api/data")
def get_users():
    app.logger.info("GET /api/data called")
    users = User.query.all()

    data = [{"id": user.id, "name": user.name} for user in users]
    return jsonify(data)



if __name__ == "__main__":
    with app.app_context():
        wait_for_db()
        db.create_all()
        seed_users()

    app.run(host="0.0.0.0", port=5000, debug=True)









