#!/usr/bin/env python3

from flask import Flask
from flask_migrate import Migrate
from models import db, Employee, Onboarding, Review

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True  # Ensure JSON is pretty-printed

migrate = Migrate(app, db)
db.init_app(app)

# Import routes here if you have separate route files
# from . import routes

if __name__ == "__main__":
    app.run(port=5555, debug=True)
