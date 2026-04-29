import uuid
from flask_sqlalchemy import SQLAlchemy
import psycopg2

db = SQLAlchemy()

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres",  # change if needed
        port=5432
    )

class Student(db.Model):
    __tablename__ = 'students'

    student_id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    monitored_by = db.Column(db.String, nullable=False)