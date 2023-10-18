from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask:flask@db:3306/flask'

db = SQLAlchemy(app)


with app.app_context():
    from routes.main import *
    from routes.employees import *
    from routes.departments import *
    from models import Employees, Departaments
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)